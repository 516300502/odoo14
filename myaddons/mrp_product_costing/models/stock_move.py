# -*- coding: utf-8 -*-

from odoo import api, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model
    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id, description):
        res = super()._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, description)
        for line in res:
            if self.production_id:
                line[2]["manufacture_order_id"] = self.production_id.id
            elif self.raw_material_production_id:
                line[2]["manufacture_order_id"] = self.raw_material_production_id.id
        return res
