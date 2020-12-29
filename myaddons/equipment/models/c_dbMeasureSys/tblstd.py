# -*- coding: utf-8 -*-
"""
@Time    : 12/21/2020 9:15 PM
@Author  : yuanlixiang
@description: C
"""
from odoo import models, fields, api


class Tblstd(models.Model):
    _name = 'tblstd'
    _description = 'tblstd'

    fcx_kind = fields.Selection([('1', 'FCX-C'),
                                 ('2', 'FCX-A'),
                                 ('3', 'FCX-AⅡ')
                                 ], string='类型')
    kindno = fields.Selection([('1', '压力计&绝对压力计用'),
                               ('2', '差压计用'),
                               ('3', '压力计(500Kg)用'),
                               ('4', '微压力计用'),
                               ], string='计用类型')
    stddate = fields.Date(string='前回登陆日')
    std1_c_min = fields.Integer(string='硅SH200 C1、C2容量下限')
    std1_c_max = fields.Integer(string='硅SH200 C1、C2容量上限')
    std1_tan = fields.Char(string='硅SH200 TAN以下')
    std1_c = fields.Float(string='SH-2以下硅')
    std2_c_min = fields.Integer(string='矿物质二聚乙C1，C2容量下限')
    std2_c_max = fields.Integer(string='矿物质二聚乙C1，C2容量上限')
    std2_tan = fields.Char(string='含矿物质TAN以下')
    std2_c = fields.Integer(string='矿物质二聚乙C1-C2以下')
    std3_c_min = fields.Float(string='二氟乙烯C1，C2容量下限')
    std3_c_max = fields.Float(string='二氟乙烯C1，C2容量上限')
    std3_tan = fields.Char(string='戴弗尔TAN以下')
    std3_c = fields.Float(string='二代胶C1-C2以下')










