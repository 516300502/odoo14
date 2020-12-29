# -*- coding: utf-8 -*-
"""
@Time    : 12/23/2020 10:00 PM
@Author  : yuanlixiang
@description: RANG量程
"""
from odoo import models, fields, api


class Sehin_Data(models.Model):
    _name = 'sehin.data'
    _description = 'Sehin Data'

    kiban = fields.Char(string='设备编号')
    pilc = fields.Char(string='格式')
    seiban = fields.Char(string='制番/POS')
    tagno = fields.Char(string='TAG.NO')
    itemno = fields.Char(string='ITEM.NO')
    baserange = fields.Char(string='基本比例范围')
    fullrange = fields.Char(string='全比例范围')
    basedata = fields.Char(string='实际刻度基础尺寸LCD')
    fulldata = fields.Char(string='实际刻度全尺寸LCD')
    softver = fields.Selection([('0', '有'),
                                ('1', '无'),
                                ], string='SoftVersion有无显示')
    tani = fields.Char(string='单位')
    romver = fields.Char(string='产品软件版本数')
    tantou = fields.Char(string='负责人')
    sikendoc = fields.Char(string='负责人')
    bodyno = fields.Char(string='bodyno')
    komano = fields.Char(string='帧No')
    ondo = fields.Char(string='溫度')
    situdo = fields.Char(string='湿度')
    kiatu = fields.Char(string='气压')
    ampunit = fields.Char(string='放大器连接器No')
    conecter = fields.Char(string='中继连接器批次No') #中継コネクタロットＮｏ
    ampsirial = fields.Char(string='放大器序列号') #アンプシリアルＮｏ
    bernout = fields.Char(string='出界')
    bernsiyo = fields.Selection([('0', '标准'),
                                 ('1', '特殊'),
                                 ], string='输出规格')
    pswlock = fields.Char(string='Psw锁定')
    cutpoint = fields.Char(string='切点')
    cutunder = fields.Selection([('0', 'LIN'),
                                 ('1', 'ZERO'),
                                 ], string='切入点')
    sokuten = fields.Selection([('0', '25%'),
                                ('1', '20%'),
                                ('2', '25%手动输入'),
                                ('3', '20%手动输入'),
                                ], string='测量点边界')
    sikenday = fields.Char(string='实验日')
    writeday = fields.Char(string='登录日')
    updateday = fields.Char(string='变更日')
    yobi = fields.Char(string='')
    bikou = fields.Char(string='备注')
    kanryoday = fields.Char(string='测试结束日')
    sikenkeka = fields.Selection([('0', '未测试'),
                                  ('1', '良品'),
                                  ('2', '不良品'),
                                  ], string='测试结果')
    sikensyu = fields.Char(string='测试类型')
    tani2 = fields.Char(string='单位数据')
    sikent = fields.Char(string='时间')
    udf = fields.Integer()
    lineno = fields.Integer()
    fe_seiban = fields.Char(string='制番/POS INDEX设定')
