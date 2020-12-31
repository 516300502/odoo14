# -*- coding: utf-8 -*-
"""
@Time    : 12/25/2020 14:00 PM
@Author  : yuanlixiang
@description: 温调，(产品信息)製品情報
"""
from odoo import models, fields, api


class Product_Information(models.Model):
    _name = 'product.information'
    _description = '产品信息'


    bodyno = fields.Char(string='bodyno')
    sikenday = fields.Date(string='实验日期')
    sikentime = fields.Char(string='实验时间点')
    test_result = fields.Char(string='实验结果')
    kaisuu = fields.Char(string='测试次数')
    precision = fields.Char(string='高精度判定')
    portno = fields.Char(string='PortNo')
    llno = fields.Char(string='ｺﾏNo')
    pilc = fields.Char(string='')
    way_to_distinguish = fields.Char(string='方式区分')
    exper_end_day = fields.Date(string='实验日期')
    exper_endtime = fields.Char(string='实验时间点')
    result = fields.Char(string='最终结果')
    rngno = fields.Integer(string='炉号')
    affirm_result = fields.Char(string='确认结果')









