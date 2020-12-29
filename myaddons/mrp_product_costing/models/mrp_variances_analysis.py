# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from datetime import date


class MrpProduction(models.Model):
    _inherit = 'mrp.production'


    def action_variances_postings(self):
        for record in self:
            quantity = record.qty_produced
            record._planned_variance_postings(quantity)
            record._material_costs_variance_postings(quantity)
            record._direct_costs_variance_postings(quantity)
        return True

    # production planned variance costs posting
    def _planned_variance_postings(self, quantity):
        final_date = False
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            planned_cost = record.prod_std_cost
            standard_cost = record.cur_std_direct_cost
            delta = round((standard_cost - planned_cost) * quantity, 2)
            desc_bom = str(record.name)
            if delta < 0.0:
                id_created_header = self.env['account.move'].create({
                'journal_id' : record.company_id.manufacturing_journal_id.id,
                'date': final_date,
                'ref' : "Planned Costs Variance",
                'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.planned_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': - delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_planned_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': - delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
            elif delta > 0.0:
                id_created_header = self.env['account.move'].create({
                'journal_id' : record.company_id.manufacturing_journal_id.id,
                'date': final_date,
                'ref' : "Planned Costs Variance",
                'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_planned_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.planned_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
        return True

    # production material and by product variance costs posting
    def _material_costs_variance_postings(self, quantity):
        final_date = False
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            mat_actual_amount = (record.mat_cost_unit - record.by_product_unit_amount) * quantity
            mat_planned_amount = (record.cur_std_mat_cost - record.cur_std_byproduct_amount) * quantity
            delta = round(mat_actual_amount - mat_planned_amount, 2)
            desc_bom = str(record.name)
            if delta < 0.0:
                id_created_header = self.env['account.move'].create({
                    'journal_id' : record.company_id.manufacturing_journal_id.id,
                    'date': final_date,
                    'ref' : "Material and By Products Variance",
                    'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.material_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': - delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_material_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': - delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
            elif delta > 0.0:
                id_created_header = self.env['account.move'].create({
                    'journal_id' : record.company_id.manufacturing_journal_id.id,
                    'date': final_date,
                    'ref' : "Material and By Products Variance",
                    'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_material_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.material_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
        return True

    # production direct variance costs posting
    def _direct_costs_variance_postings(self, quantity):
        final_date = False
        for record in self:
            if record.date_actual_finished_wo:
                final_date = record.date_actual_finished_wo.date()
            else:
                final_date = date.today()
            direct_actual_amount = (record.lab_cost_unit + record.fixed_cost_unit) * quantity
            direct_planned_amount = (record.cur_std_lab_cost + record.cur_std_fixed_cost) * quantity
            delta = round(direct_actual_amount - direct_planned_amount, 2)
            desc_bom = str(record.name)
            if delta < 0.0:
                id_created_header = self.env['account.move'].create({
                    'journal_id' : record.company_id.manufacturing_journal_id.id,
                    'date': final_date,
                    'ref' : "Direct Costs Variance",
                    'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.other_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': - delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_direct_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': - delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
            elif delta > 0.0:
                id_created_header = self.env['account.move'].create({
                    'journal_id' : record.company_id.manufacturing_journal_id.id,
                    'date': final_date,
                    'ref' : "Direct Costs Variance",
                    'company_id': record.company_id.id,
                })
                id_credit_item = self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.product_id.property_stock_production.valuation_out_account_id.id,
                    'analytic_account_id' : record.bom_id.costs_direct_variances_analytic_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': delta,
                    'debit': 0.0,
                    'manufacture_order_id': record.id,
                })
                id_debit_item= self.env['account.move.line'].with_context(check_move_validity=False).create({
                    'move_id' : id_created_header.id,
                    'account_id': record.company_id.other_variances_account_id.id,
                    'product_id': record.product_id.id,
                    'name' : desc_bom,
                    'quantity': quantity,
                    'product_uom_id': record.product_uom_id.id,
                    'credit': 0.0,
                    'debit': delta,
                    'manufacture_order_id': record.id,
                })
                id_created_header.post()
        return True

