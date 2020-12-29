# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    costs_overhead_product_percentage = fields.Float(string=_('OVH Costs Product percentage'), default="0.0")
    costs_overhead_components_percentage = fields.Float(string=_('OVH Costs Components percentage'), default="0.0")
    analytic_account_id = fields.Many2one('account.analytic.account', string=_("Cost Analytic Account"))
    costs_planned_variances_analytic_account_id = fields.Many2one('account.analytic.account', string=_("Planned Variance Costs Analytic Account"))
    costs_material_variances_analytic_account_id = fields.Many2one('account.analytic.account', string=_("Material Variance Costs Analytic Account"))
    costs_direct_variances_analytic_account_id = fields.Many2one('account.analytic.account', string=_("Direct Variance Costs Analytic Account"))




