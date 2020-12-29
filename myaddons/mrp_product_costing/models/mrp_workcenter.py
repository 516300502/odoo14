# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'


    WORKCENTER_TYPE = [
        ('H', 'Man'),
        ('M', 'Machine'),
    ]

    wc_type = fields.Selection(WORKCENTER_TYPE, 'Work Center Type')
    cost_hour = fields.Float(string=_('Hourly Direct Cost Rate'), default="0.0")
    cost_hour_fixed = fields.Float(string=_('Hourly Fixed Direct Cost Rate'), default="0.0")
    costs_overhead_variable_percentage = fields.Float(string=_('Variable OVH Costs percentage'), default="0.0")
    costs_overhead_fixed_percentage = fields.Float(string=_('Fixed OVH Costs percentage'), default="0.0")
    analytic_account_id = fields.Many2one('account.analytic.account', string=_("Cost Analytic Account"))
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id.id)



