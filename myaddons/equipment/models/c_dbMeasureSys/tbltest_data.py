# -*- coding: utf-8 -*-
"""
@Time    : 12/21/2020 9:15 PM
@Author  : yuanlixiang
@description: C
"""
from odoo import models, fields, api



class TblTestData(models.Model):
    _name = 'tbltestdata'
    _description = 'tbltestdata'

    bodyno = fields.Char(string='bodyno')
    testcnt = fields.Integer(string='最后实验bodyno的测试次数(1～9)')
    testdate = fields.Date(string='日期')
    komano = fields.Char(string='最后实验格子NO')
    stdkind = fields.Integer(string='注入液No')
    test_temp = fields.Float(string='温度')
    test_humid = fields.Float(string='湿度')
    td_c1 = fields.Float(string='C容量(PF)C1')
    td_c2 = fields.Float(string='C容量(PF)C2')
    td_c3 = fields.Float(string='C容量(PF)C1_C2')
    td_d1 = fields.Float(string='损失系数(D)C1')
    td_d2 = fields.Float(string='损失系数(D)C2')
    td_r1 = fields.Integer(string='备用')
    td_r2 = fields.Integer(string='备用')
    tr_c1 = fields.Selection([('0', '未实验'),
                                 ('1', 'NG'),
                                 ('2', 'GOOD')
                                 ], string='C容量(PF)_C1')
    tr_c2 = fields.Selection([('0', '未实验'),
                                 ('1', 'NG'),
                                 ('2', 'GOOD')
                                 ], string='C容量(PF)_C2')
    tr_c3 = fields.Selection([('0', '未实验'),
                                 ('1', 'NG'),
                                 ('2', 'GOOD')
                                 ], string='C容量(PF)_C1-C2')
    tr_d1 = fields.Selection([('0', '未实验'),
                                 ('1', 'NG'),
                                 ('2', 'GOOD')
                                 ], string='损失系数(D)_C1')
    tr_d2 = fields.Selection([('0', '未实验'),
                                 ('1', 'NG'),
                                 ('2', 'GOOD')
                                 ], string='损失系数(D)_C2')
    tr_r1 = fields.Integer(string='备用')
    tr_r2 = fields.Integer(string='备用')
    test_result = fields.Selection([('1', 'NG'),
                                    ('2', 'GOOD'),
                                    ], string='综合结果')
    udf = fields.Integer()