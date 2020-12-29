# -*- coding: utf-8 -*-
"""
@Time    : 12/25/2020 8:40 PM
@Author  : yuanlixiang
@description: 温调，温度实验(10,20,30,50,85)
"""
from odoo import models, fields, api


class Test_Degree_Centigrade(models.Model):
    _name = 'test.degree.centigrade'
    _description = '10,20,30,50,85℃实验'

    bodyno = fields.Char(string='bodyno')
    mp1mst = fields.Float(string='')
    mp2mst = fields.Float(string='')
    mp3mst = fields.Float(string='')
    mp4mst = fields.Float(string='')
    mp5mst = fields.Float(string='')
    t11 = fields.Float()
    t12 = fields.Float()
    t13 = fields.Float()
    t14 = fields.Float()
    t15 = fields.Float()
    t21 = fields.Float()
    t22 = fields.Float()
    t23 = fields.Float()
    t24 = fields.Float()
    t25 = fields.Float()
    t3 = fields.Float()
    t4 = fields.Float()
    lka = fields.Float()
    tnc = fields.Float()
    ds10 = fields.Float()
    pvzw = fields.Float()
    pvsw = fields.Float()
    mv1 = fields.Float()
    mv2 = fields.Float()
    mv3 = fields.Float()
    mv4 = fields.Float()
    mv5 = fields.Float()
    mp1 = fields.Float()
    mp2 = fields.Float()
    mp3 = fields.Float()
    mp4 = fields.Float()
    mp5 = fields.Float()
    errflg = fields.Char(string='')
    lpv_positive = fields.Float()
    lpv_negative = fields.Float()
    spv_negative = fields.Float()
    zpv_positive = fields.Float()
    tpv = fields.Float()
    adjust_pv = fields.Float()
    exchange_pv = fields.Float()
    test_ex = fields.Char(string='')
    temperature_type = fields.Selection([('10', '10摄氏度'),
                                         ('20', '20摄氏度'),
                                         ('30', '30摄氏度'),
                                         ('50', '50摄氏度'),
                                         ('85', '80摄氏度')
                                         ], string='温度类型')


class Affirm_Degree_Centigrade(models.Model):
    _name = 'affirm.degree.centigrade'
    _description = '10,85℃实验'

    bodyno = fields.Char(string='bodyno')
    lka = fields.Float()
    tnc = fields.Float()
    mv1 = fields.Float()
    mv2 = fields.Float()
    mv3 = fields.Float()
    mv4 = fields.Float()
    mv5 = fields.Float()
    mp1 = fields.Float()
    mp2 = fields.Float()
    mp3 = fields.Float()
    mp4 = fields.Float()
    mp5 = fields.Float()
    errflg = fields.Char(string='')
    lpv_positive = fields.Float()
    lpv_negative = fields.Float()
    spv_negative = fields.Float()
    zpv_positive = fields.Float()
    tpv = fields.Float()
    exchange_pv = fields.Float()
    test_ex = fields.Char(string='')
    lpv20_positive = fields.Float()
    lpv20_negative = fields.Float()
    spv20_negative = fields.Float()
    zpv20_positive = fields.Float()
    tpv20 = fields.Float()
    temperature_type = fields.Selection([('10', '10摄氏度'),
                                         ('85', '80摄氏度')
                                         ], string='温度类型')




class Affirm_Degree_Centigrade20(models.Model):
    _name = 'affirm.degree.centigrade20'
    _description = '确认返回20℃测试'

    bodyno = fields.Char(string='bodyno')
    mv1 = fields.Float()
    mv2 = fields.Float()
    mv3 = fields.Float()
    mv4 = fields.Float()
    mv5 = fields.Float()
    mp1 = fields.Float()
    mp2 = fields.Float()
    mp3 = fields.Float()
    mp4 = fields.Float()
    mp5 = fields.Float()
    daz = fields.Float()
    das = fields.Float()
    mvl = fields.Float()
    mvh = fields.Float()
    tocz1 = fields.Float()
    tocz2 = fields.Float()
    tocz3 = fields.Float()
    tocz4 = fields.Float()
    tocs1 = fields.Float()
    tocs2 = fields.Float()
    tocs3 = fields.Float()
    tocs4 = fields.Float()
    lka = fields.Float()
    k = fields.Float()
    pnz = fields.Float()
    pns = fields.Float()
    tm40c = fields.Float()
    tm10c = fields.Float()
    t20c = fields.Float()
    t50c = fields.Float()
    t85c = fields.Float()
    tka1 = fields.Float()
    tka2 = fields.Float()
    tka3 = fields.Float()
    tka4 = fields.Float()
    tkb1 = fields.Float()
    tkb2 = fields.Float()
    tkb3 = fields.Float()
    tkb4 = fields.Float()
    ezm40c = fields.Float()
    esm40c = fields.Float()
    ezm10c = fields.Float()
    esm10c = fields.Float()
    ez50c = fields.Float()
    es50c = fields.Float()
    ez85c = fields.Float()
    es85c = fields.Float()
    errcode40 = fields.Float()
    errcode10 = fields.Float()
    errcode20 = fields.Float()
    errcode50 = fields.Float()
    errcode85 = fields.Float()
    precision = fields.Char(string='高精度判定')
    good_or_no = fields.Char(string='良否判定')
    modality = fields.Float()
    lkm1 = fields.Float()
    lkm2 = fields.Float()
    lkm3 = fields.Float()
    lkm4 = fields.Float()
    tcms1 = fields.Float()
    tcms2 = fields.Float()
    tcms3 = fields.Float()
    tcms4 = fields.Float()
    lpv_positive = fields.Float()
    lpv_negative = fields.Float()
    spv_negative = fields.Float()
    zpv_positive = fields.Float()
    tpv = fields.Float()
    adjust_pv = fields.Float()
    exchange_pv = fields.Float()
    test_ex = fields.Char(string='')
    mp1mst = fields.Float()
    mp2mst = fields.Float()
    mp3mst = fields.Float()
    mp4mst = fields.Float()
    mp5mst = fields.Float()
    pvz = fields.Float()


class Affirm_Degree_Centigrade20add(models.Model):
    _name = 'affirm.degree.centigrade20.add'
    _description = '返回20℃试验追加'


    bodyno = fields.Char(string='bodyno')
    mp1mst = fields.Float()
    mp2mst = fields.Float()
    mp3mst = fields.Float()
    mp4mst = fields.Float()
    mp5mst = fields.Float()
    t11 = fields.Float()
    t12 = fields.Float()
    t13 = fields.Float()
    t14 = fields.Float()
    t15 = fields.Float()
    t21 = fields.Float()
    t22 = fields.Float()
    t23 = fields.Float()
    t24 = fields.Float()
    t25 = fields.Float()
    t3 = fields.Float()
    t4 = fields.Float()
    vrfrslt = fields.Float()






















