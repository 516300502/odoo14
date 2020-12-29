# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    manufacture_order_id = fields.Many2one("mrp.production", string="Manufacturing Order", copy=False, index=True)

    def _prepare_analytic_line(self):
        result = super()._prepare_analytic_line()
        for line in self:
            if line.manufacture_order_id:
                result[0]["manufacture_order_id"] = line.manufacture_order_id.id
        return result

