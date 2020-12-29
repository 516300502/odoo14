# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    planned_variances_account_id = fields.Many2one('account.account', string="Planned Variance Cost Account")
    material_variances_account_id = fields.Many2one('account.account', string="Material Variance Cost Account")
    other_variances_account_id = fields.Many2one('account.account', string="Other Variance Cost Account")
    labour_cost_account_id = fields.Many2one('account.account', string="Labour Cost Account")
    machine_run_cost_account_id = fields.Many2one('account.account', string="Machine Run Cost Account")
    manufacturing_journal_id = fields.Many2one('account.journal', string="Manufacturing journal id")
    cost_analytic_account_id = fields.Many2one('account.analytic.account', string="Cost Collector Analytic Account")


class MrpProdCostParameters (models.TransientModel):
    _name = 'mrp.product.costing.parameters'
    _description = 'mrp product costing setting'
    _rec_name = "company_id"

    planned_variances_account_id = fields.Many2one('account.account', string=_("Planned Variance Cost Account*"), related="company_id.planned_variances_account_id", readonly=False)
    material_variances_account_id = fields.Many2one('account.account', string=_("Material Variances Cost Account*"), related="company_id.material_variances_account_id", readonly=False)
    other_variances_account_id = fields.Many2one('account.account', string=_("Other Variances Cost Account*"), related="company_id.other_variances_account_id", readonly=False)
    labour_cost_account_id = fields.Many2one('account.account', string=_("Labour Cost Account*"), related="company_id.labour_cost_account_id", readonly=False)
    machine_run_cost_account_id = fields.Many2one('account.account', string=_("Machine Run Cost Account*"), related="company_id.machine_run_cost_account_id", readonly=False)
    manufacturing_journal_id = fields.Many2one('account.journal', string=_("Manufacturing journal id*"), related="company_id.manufacturing_journal_id", readonly=False)
    cost_analytic_account_id = fields.Many2one('account.analytic.account', string=_("Cost Collector Analytic Account*"), related="company_id.cost_analytic_account_id", readonly=False)
    company_id = fields.Many2one('res.company', string=_('Company'), required=True, default=lambda self: self.env.user.company_id)
