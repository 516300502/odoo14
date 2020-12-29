# -*- coding: utf-8 -*-
"""
@Time    : 12/22/2020 9:00 PM
@Author  : yuanlixiang
@description: line直线
"""
from odoo import models, fields, api


class Sampl_Data(models.Model):
    _name = 'sampl.data'
    _description = 'Sampl Data'

    bodyno = fields.Char(string='bodyno')
    kai = fields.Integer(string='试验次数')
    t1p0 = fields.Integer(string='T1 (0%),(-100%)$200F～3BYTE')
    t1p1 = fields.Integer(string='T1 (25%),(-50%)$2012～3BYTE')
    t1p2 = fields.Integer(string='T1 (50%),(0%)$2015～3BYTE')
    t1p3 = fields.Integer(string='T1 (75%),(50%)$2018～3BYTE')
    t1p4 = fields.Integer(string='T1 (100%),(100%)$201B～3BYTE')
    t2p0 = fields.Integer(string='T2 (0%),(-100%)$201E～3BYTE')
    t2p1 = fields.Integer(string='T2 (25%),(-50%)$2021～3BYTE')
    t2p2 = fields.Integer(string='T2 (50%),(0%)$2024～3BYTE')
    t2p3 = fields.Integer(string='T2 (75%) (50%)$2027～3BYTE')
    t2p4 = fields.Integer(string='T2 (100%),(100%)$202A～3BYTE')
    t3 = fields.Integer(string='T3 (0%)$202D～3BYTE')
    mstp0 = fields.Float(string='P0 (0%),(-100%)$2030～3BYTE')
    mstp1 = fields.Float(string='P1 (25%),(-50%)$2038～3BYTE')
    mstp2 = fields.Float(string='P2 (50%),(0%)$2040～3BYTE')
    mstp3 = fields.Float(string='P3 (75%),(50%)$2064～3BYTE')
    mstp4 = fields.Float(string='P4 (100%),(100%)$206C～3BYTE')
    pnz = fields.Integer(string='传感器调整数据$2007～3BYTE')
    pns = fields.Float(string='调整数据$200A～3BYTE')
    lineno = fields.Char(string='')
    siken_dts = fields.Date(string='日期/时间')
