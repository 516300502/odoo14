# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    
    analytic_account_id = fields.Many2one('account.analytic.account', string=_('Analytic Account'), readonly=True, states={'draft': [('readonly', False)]})
    
    prod_std_cost = fields.Float(digits='Product Price', string=_('Current Standard Cost'), compute='calculate_planned_costs', store=True, 
        group_operator="avg")
    cur_std_mat_cost = fields.Float(digits='Product Price', string=_('Planned Material Unit Cost'), compute='calculate_planned_costs', store=True, 
        group_operator="avg")
    cur_std_lab_cost = fields.Float(digits='Product Price', string=_('Planned Direct Variable Unit Cost'), compute='calculate_planned_costs', store=True, 
        group_operator="avg")
    cur_std_fixed_cost = fields.Float(digits='Product Price', string=_('Planned Direct Fixed Unit Cost'), compute='calculate_planned_costs', store=True, 
        group_operator="avg")
    cur_std_direct_cost = fields.Float(digits='Product Price', string=_('Planned Direct Unit Cost'), compute='calculate_planned_costs', store=True, 
        group_operator="avg")
    cur_std_byproduct_amount = fields.Float(digits='Product Price', string=_('Planned ByProduct Amount'), compute='calculate_planned_by_product_amount', store=True)
        
    mat_cost = fields.Float(digits='Product Price', string=_('Actual Material Cost'), compute='calculate_material_cost', store=True)
    mat_cost_unit = fields.Float(digits='Product Price', string=_('Actual Material Unit Cost'), compute='calculate_material_cost', store=True, group_operator="avg")
    lab_cost = fields.Float(digits='Product Price', string=_('Actual Direct Variable Cost'), compute='calculate_actual_costs', store=True)
    lab_cost_unit = fields.Float(digits='Product Price', string=_('Actual Direct Variable Unit Cost'), compute='calculate_actual_costs', store=True, 
        group_operator="avg")
    fixed_cost = fields.Float(digits='Product Price', string=_('Actual Direct Fixed Cost'), compute='calculate_actual_costs', store=True)
    fixed_cost_unit = fields.Float(digits='Product Price', string=_('Actual Direct Fixed Unit Cost'), compute='calculate_actual_costs', store=True, 
        group_operator="avg")
    direct_cost = fields.Float(digits='Product Price', string=_('Actual Full Direct Cost'), compute='calculate_actual_costs', store=True)
    direct_cost_unit = fields.Float(digits='Product Price', string=_('Actual Full Direct Unit Cost'), compute='calculate_actual_costs', store=True, group_operator="avg")
    by_product_amount = fields.Float(digits='Product Price', string=_('Actual ByProduct Amount'), compute='calculate_actual_by_product_amount', store=True)
    by_product_unit_amount = fields.Float(digits='Product Price', string=_('Actual ByProduct Unit Amount'), compute='calculate_actual_by_product_amount', store=True, 
        group_operator="avg")
    
    delta_mat_cost = fields.Float(digits='Product Price', string=_('Delta Material Unit Cost'), compute='calculate_delta_unit_costs', store=True)
    delta_lab_cost = fields.Float(digits='Product Price', string=_('Delta Direct Variable Unit Cost'), compute='calculate_delta_unit_costs', store=True)
    delta_fixed_cost = fields.Float(digits='Product Price', string=_('Delta Direct Fixed Unit Cost'), compute='calculate_delta_unit_costs', store=True)
    delta_direct_cost = fields.Float(digits='Product Price', string=_('Delta Direct Unit Cost'), compute='calculate_delta_unit_costs', store=True)
    delta_byproduct = fields.Float(digits='Product Price', string=_('Delta ByProduct Amount'), compute='calculate_delta_unit_costs', store=True)
    
    wip_amount = fields.Float(digits='Product Price', string=_('WIP Amount'), compute='calculate_wip_amount', store=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id.id)
    
    
    @api.depends('state')
    def calculate_wip_amount(self):
        wipamount = 0.0
        for production in self:
            if production.state != 'done':
                wipamount = production.mat_cost + production.lab_cost + production.fixed_cost
            production.wip_amount = wipamount
        return True
    
    @api.depends('product_id','bom_id', 'cur_std_byproduct_amount') #'routing_id'
    def calculate_planned_costs(self):
        costmat = 0.0
        costlab = 0.0
        costfixed = 0.0
        for production in self:
            result, result2 = production.bom_id.explode(production.product_id, 1)
            for sbom, sbom_data in result2:
                costmat += sbom.product_id.standard_price * sbom_data['qty']
            # if production.routing_id:
            #     for activity in production.routing_id.operation_ids:
            #         costlab += (activity.time_cycle/60) * activity.workcenter_id.costs_hour
            #         costfixed += (activity.workcenter_id.time_stop + activity.workcenter_id.time_start) * activity.workcenter_id.cost_hour_fixed / 60
            production.prod_std_cost = production.product_id.standard_price
            production.cur_std_mat_cost = costmat
            production.cur_std_lab_cost = costlab
            production.cur_std_fixed_cost = costfixed
            production.cur_std_direct_cost = costlab + costfixed + costmat - production.cur_std_byproduct_amount
        return True
        
    @api.depends('move_finished_ids.state','bom_id')     
    def calculate_planned_by_product_amount(self):
        byproductamount = 0.0
        for production in self:
            for byproduct_id in production.bom_id.byproduct_ids:
                byproductamount += byproduct_id.product_id.standard_price * byproduct_id.product_qty
            production.cur_std_byproduct_amount = byproductamount
        return True

    @api.depends('move_raw_ids','qty_produced')
    def calculate_material_cost(self):
        matprice = 0.0
        matamount = 0.0
        qty_produced = 1.0
        for production in self:
            for move in production.move_raw_ids:
                matamount += move.product_id.standard_price * move.quantity_done
            if production.product_id  and not production.product_qty == 0.0:
                if production.qty_produced == 0.0:
                    qty_produced = production.product_qty
                else:
                    qty_produced = production.qty_produced
            matprice = matamount / qty_produced
            production.mat_cost = matamount
            production.mat_cost_unit = matprice 
        return True

    @api.depends('move_finished_ids.state','qty_produced')     
    def calculate_actual_by_product_amount(self):
        receiptamount = 0.0
        qty_produced = 1.0
        for production in self:
            if production.bom_id.byproduct_ids:
                moves = production.move_finished_ids.filtered(lambda r: r.state == 'done')
                for move in moves:
                    receiptamount += move.product_id.standard_price * move.quantity_done
                if receiptamount:
                    production.by_product_amount = receiptamount - production.prod_std_cost * production.qty_produced
            else:
                production.by_product_amount = 0.0
            if production.product_id  and not production.product_qty == 0.0:
                if production.qty_produced == 0.0:
                    qty_produced = production.product_qty
                else:
                    qty_produced = production.qty_produced
            production.by_product_unit_amount = production.by_product_amount / qty_produced
        return True

    @api.depends('workorder_ids.time_ids', 'qty_produced', 'mat_cost_unit', 'mat_cost', 'by_product_amount')
    def calculate_actual_costs(self):
        labcost = 0.0
        labamount = 0.0
        fixcost = 0.0
        fixedamount = 0.0
        qty_produced = 1.0
        for production in self:
            for workorder in production.workorder_ids:
                labtime = 0.0
                fixedtime = 0.0
                for time in workorder.time_ids:
                    if time.overall_duration:
                        labtime += time.working_duration
                        fixedtime += time.setup_duration + time.teardown_duration
                    else:
                        labtime += time.duration
                labamount += labtime * workorder.workcenter_id.cost_hour / 60
                fixedamount += fixedtime * workorder.workcenter_id.cost_hour_fixed / 60
            if production.product_id and not production.product_qty == 0.0:
                if production.qty_produced == 0.0:
                    qty_produced = production.product_qty
                else:
                    qty_produced = production.qty_produced
            labcost = labamount / qty_produced
            fixcost = fixedamount / qty_produced
        production.lab_cost = labamount 
        production.lab_cost_unit = labcost
        production.fixed_cost = fixedamount
        production.fixed_cost_unit = fixcost
        production.direct_cost = fixedamount + labamount + production.mat_cost - production.by_product_amount
        production.direct_cost_unit = labcost + fixcost + production.mat_cost_unit - production.by_product_unit_amount
        return True
    
    @api.depends('mat_cost_unit','lab_cost_unit','direct_cost_unit')
    def calculate_delta_unit_costs(self):
        for production in self:
            production.delta_mat_cost = - (production.cur_std_mat_cost - production.mat_cost_unit)
            production.delta_lab_cost = - (production.cur_std_lab_cost - production.lab_cost_unit)
            production.delta_fixed_cost = - (production.cur_std_fixed_cost - production.fixed_cost_unit)
            production.delta_direct_cost = - (production.cur_std_direct_cost - production.direct_cost_unit)
            production.delta_byproduct = - (production.cur_std_byproduct_amount - production.by_product_unit_amount)
        return True
