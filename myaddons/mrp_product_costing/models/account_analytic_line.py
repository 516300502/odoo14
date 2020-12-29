# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    manufacture_order_id = fields.Many2one("mrp.production", string="Manufacturing Order", copy=False, index=True)
