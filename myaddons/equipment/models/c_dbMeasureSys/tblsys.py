# -*- coding: utf-8 -*-
"""
@Time    : 12/21/2020 9:15 PM
@Author  : yuanlixiang
@description: C
"""
from odoo import models, fields, api



class Tblsys(models.Model):
    _name = 'tblsys'
    _description = 'tblsys'

    bodyno = fields.Char(string='bodyno')
    testcnt = fields.Integer(string='最后实验bodyno的测试次数(1～9)')
    komano = fields.Char(string='最后实验格子NO')
    stdkind = fields.Integer(string='最后试验的装入液NO')
    temp = fields.Float(string='温度')
    humid = fields.Float(string='湿度')
    password = fields.Char(string='规格值画面')