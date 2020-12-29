# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 15:00 PM
@Author  : yuanlixiang
@description: 温调，恒温槽
"""
from odoo import models, fields, api


class Thermostatic_Bath(models.Model):
    _name = 'thermostatic.bath'
    _description = '恒温槽'

    bodyno = fields.Char(string='bodyno')
    rngno = fields.Integer(string='炉号')
