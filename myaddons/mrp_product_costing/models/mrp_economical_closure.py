# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from datetime import date


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    variable_ovh_lab_mac_cost = fields.Float(digits='Product Price', string=_('OVH Variable Direct Cost'), readonly=True)
    fixed_ovh_lab_mac_cost = fields.Float(digits='Product Price', string=_('OVH Fixed Direct Cost'), readonly=True)
    ovh_product_cost = fields.Float(digits='Product Price', string=_('OVH Finished Product Cost'), readonly=True)
    ovh_components_cost = fields.Float(digits='Product Price', string=_('OVH Components Cost'), readonly=True)
    industrial_cost = fields.Float(digits='Product Price', string=_('Actual Full Industrial Cost'), readonly=True)
    industrial_cost_unit = fields.Float(digits='Product Price', string=_(' Actual Full Industrial Unit Cost'), group_operator="avg", readonly=True)


    def post_inventory(self):
        res = super().post_inventory()
        for record in self:
            record.action_variances_postings()
            record.action_economical_closure()
        return res

    def action_economical_closure(self):
        industrialcost = 0.0
        industrialunitcost = 0.0
        for record in self:
            record._wc_ovh_analytic_postings()
            record._bom_ovh_analytic_postings()
            record._cost_collector_analytic_postings()
            industrialcost = record.direct_cost + record.variable_ovh_lab_mac_cost + record.fixed_ovh_lab_mac_cost + record.ovh_product_cost + record.ovh_components_cost
            if record.product_id  and not record.product_qty == 0.0 and not record.qty_produced == 0.0:
                industrialunitcost = industrialcost / record.qty_produced
            record.industrial_cost = industrialcost
            record.industrial_cost_unit = industrialunitcost
        return True

    def _wc_ovh_analytic_postings(self):
        final_date = False
        fixedlabcost = 0.0
        variablelabcost = 0.0
        timevariable = 0.0
        timefixed = 0.0
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            for workorder in record.workorder_ids:
                desc_wo = str(record.name) + '-' + str(workorder.workcenter_id.name) + '-' + str(workorder.name)
                for time in workorder.time_ids:
                    timevariable += time.working_duration
                    timefixed += time.setup_duration + time.teardown_duration
                variablelabcost += timevariable * workorder.workcenter_id.cost_hour / 60 * (workorder.workcenter_id.costs_overhead_variable_percentage / 100)
                fixedlabcost += timefixed * (workorder.workcenter_id.cost_hour_fixed / 60) * (workorder.workcenter_id.costs_overhead_fixed_percentage / 100)
                # fixed direct overhead cost posting
                if fixedlabcost:
                    id_created= self.env['account.analytic.line'].create({
                        'name': desc_wo,
                        'account_id': workorder.workcenter_id.analytic_account_id.id,
                        'ref': "OVH other fixed direct costs",
                        'date': final_date,
                        'product_id': record.product_id.id,
                        'amount': fixedlabcost,
                        'unit_amount': record.qty_produced,
                        'product_uom_id': record.product_uom_id.id,
                        'company_id': workorder.workcenter_id.company_id.id,
                        'manufacture_order_id': record.id,
                    })
                # variable direct overhead cost posting
                if variablelabcost:
                    id_created= self.env['account.analytic.line'].create({
                        'name': desc_wo,
                        'account_id': workorder.workcenter_id.analytic_account_id.id,
                        'ref': "OVH other variable direct costs",
                        'date': final_date,
                        'product_id': record.product_id.id,
                        'amount': variablelabcost,
                        'unit_amount': record.qty_produced,
                        'product_uom_id': record.product_uom_id.id,
                        'company_id': workorder.workcenter_id.company_id.id,
                        'manufacture_order_id': record.id,
                    })
            record.variable_ovh_lab_mac_cost = variablelabcost
            record.fixed_ovh_lab_mac_cost = fixedlabcost
        return True

    def _bom_ovh_analytic_postings(self):
        ovhproductcost = 0.0
        ovhcomponentscost = 0.0
        final_date = False
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            desc_bom = str(record.name)
            ovhproductcost = record.qty_produced * record.prod_std_cost * (record.bom_id.costs_overhead_product_percentage / 100)
            ovhcomponentscost = record.mat_cost * (record.bom_id.costs_overhead_components_percentage / 100)
            # overhead product cost posting
            if ovhproductcost:
                id_created= self.env['account.analytic.line'].create({
                    'name': desc_bom,
                    'account_id': record.bom_id.analytic_account_id.id,
                    'ref': "OVH production costs",
                    'date': final_date,
                    'product_id': record.product_id.id,
                    'amount': - ovhproductcost,
                    'unit_amount': record.qty_produced,
                    'product_uom_id': record.product_uom_id.id,
                    'company_id': record.company_id.id,
                    'manufacture_order_id': record.id,
                })
            # overhead components cost posting
            if ovhcomponentscost:
                id_created= self.env['account.analytic.line'].create({
                    'name': desc_bom,
                    'account_id': record.bom_id.analytic_account_id.id,
                    'ref': "OVH components costs",
                    'date': final_date,
                    'product_id': record.product_id.id,
                    'amount': - ovhcomponentscost,
                    'unit_amount': record.qty_produced,
                    'product_uom_id': record.product_uom_id.id,
                    'company_id': record.company_id.id,
                    'manufacture_order_id': record.id,
                })
            record.ovh_product_cost = ovhproductcost
            record.ovh_components_cost = ovhcomponentscost
        return True

    # overhead cost collector product cost posting
    def _cost_collector_analytic_postings(self):
        final_date = False
        overall_overhead_cost_amount = 0.0
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            desc_bom = str(record.name)
            overall_overhead_cost_amount = record.variable_ovh_lab_mac_cost + record.fixed_ovh_lab_mac_cost + record.ovh_product_cost + record.ovh_components_cost
            if overall_overhead_cost_amount:
                id_created= self.env['account.analytic.line'].create({
                    'name': desc_bom,
                    'account_id': record.company_id.cost_analytic_account_id.id,
                    'ref': "cost collector overhead costs",
                    'date': final_date,
                    'product_id': record.product_id.id,
                    'amount': overall_overhead_cost_amount,
                    'unit_amount': record.qty_produced,
                    'product_uom_id': record.product_uom_id.id,
                    'company_id': record.company_id.id,
                    'manufacture_order_id': record.id,
                })
        return True
