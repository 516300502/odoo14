# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 15:00 PM
@Author  : yuanlixiang
@description: 温调，(校正数据)補正データ
"""
from odoo import models, fields, api


class Correction_Data(models.Model):
    _name = 'correction.data'
    _description = '校正数据'


    bodyno = fields.Char(string='bodyno')
    splka20 = fields.Float()
    spk20 = fields.Float()
    splka50 = fields.Float()
    tnc50 = fields.Float()
    splka85 = fields.Float()
    tnc85 = fields.Float()
    splkam10 = fields.Float()
    tncm10 = fields.Float()
    splkam30 = fields.Float()
    tncm30 = fields.Float()
    K2 = fields.Float()
    sppnz = fields.Float()
    sppns = fields.Float()



