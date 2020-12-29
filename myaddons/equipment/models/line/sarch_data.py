# -*- coding: utf-8 -*-
"""
@Time    : 12/22/2020 9:00 PM
@Author  : yuanlixiang
@description: line直线
"""
from odoo import models, fields, api



class Sarch_Data(models.Model):
    _name = 'sarch.data'
    _description = 'Sarch Data'

    bodyno = fields.Char(string='bodyno')
    writeday = fields.Date(string='登录日')
    sikenday = fields.Date(string='实验日')
    kekka = fields.Char(string='实验结果')
    kaisuu = fields.Char(string='测试次数')
    koma = fields.Char(string='最后实验格子NO')
    pilc = fields.Char(string='格式')
    ondo = fields.Float(string='溫度')
    situdo = fields.Float(string='湿度')
    kiatu = fields.Float(string='气压')
    yobi1 = fields.Char(string='备用')
    yobi2 = fields.Char(string='备用')
    udf = fields.Integer()
    lineno = fields.Char()