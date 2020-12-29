# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class WipAmount(models.Model):
    _inherit = 'stock.move.line'


    standard_price = fields.Float(string='当前成本')
    total_price = fields.Float(string='总成本')