# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 9:00 PM
@Author  : yuanlixiang
@description: taidt片均压
"""
from odoo import models, fields, api


class FcxRang_Siken_Data(models.Model):
    _name = 'fcxrang.siken.data'
    _description = 'FcxRang Siken Data'

    bodyno = fields.Char(string='bodyno')
    koma = fields.Char(string='最后实验格子NO')
    pilc = fields.Char(string='格式')
    sikenday = fields.Date(string='实验日')
    kaisuu = fields.Char(string='测试次数')
    yobi1 = fields.Char(string='Jig No.')
    ondo = fields.Char(string='溫度')
    situdo = fields.Char(string='湿度')
    kiatu = fields.Char(string='气压')
    sdata00 = fields.Float(string='压力计1或2')
    sdata01 = fields.Float(string='综合判定结果')  # 総合判定結果
    sdata02 = fields.Float(string='实验最后结果')  # 試験済みﾌﾗｸﾞ
    sdata03 = fields.Float(string='耐压(过大压力)气密结果')  # 耐圧（過大圧）気密結果
    sdata04 = fields.Float(string='过大压力零点变动结果')  # 過大圧ゼロ点変動結果
    sdata05 = fields.Float(string='压缩结果')  # 压缩结果
    sdata06 = fields.Float(string='均压特性综合结果')  # 均压特性综合结果
    sdata07 = fields.Float(string='均压1结果')
    sdata08 = fields.Float(string='均压2结果')
    sdata09 = fields.Float(string='空闲')  # 空き
    sdata10 = fields.Float(string='过大压力试验体大气点导程1')  # 過大圧被試験体大気点リード１
    sdata11 = fields.Float(string='施加过大压力后导程2')  # 過大圧被試験体圧力印加後リード２
    sdata12 = fields.Float(string='耐压(过大压力)判定用主大气点导程')  # 耐圧（過大圧）判定用マスター大気点リード
    sdata13 = fields.Float(string='耐压判定用主压力施加引线1')  # 耐圧判定用マスター圧力印加リード１
    sdata14 = fields.Float(string='耐压判定用主大气开放前导程')  # 耐圧判定用マスター大気開放前リード
    sdata15 = fields.Float(string='耐压判定压力计(S3′-S3′)差压计(S3′-S3′)')  # 耐圧判定 圧力計（Ｓ３”－Ｓ３’）  差圧計（Ｓ３’－Ｓ３”）
    sdata16 = fields.Float(string='单压判定值第1次')  # 片圧判定値１回目
    sdata17 = fields.Float(string='单压判定值第2次')  # 片圧判定値２回目
    sdata18 = fields.Float(string='均压测定值第1次')  # 均圧測定値１回目
    sdata19 = fields.Float(string='均压测定值第2次')  # 均圧測定値2回目
    sdata20 = fields.Float(string='均压测定值第3次')  # 均圧測定値3回目
    sdata21 = fields.Float(string='单压误差')  # 片圧誤差   （Ｓ１－Ｓ２）÷１６×１００
    sdata22 = fields.Float(string='均压误差1')  # 均圧誤差１ （Ｓ１－Ｓ２）÷１６×１００
    sdata23 = fields.Float(string='均压误差2')  # 均圧誤差2 （Ｓ１－Ｓ２）÷１６×１００
    sdata24 = fields.Float(string='过大压力零变动误差')  # 過大圧ゼロ変動誤差  （Ｓ２－Ｓ１）÷１６×１００
    sdata25 = fields.Float(string='气密计算4')  # 気密計算４
    sdata26 = fields.Float(string='')
    sdata27 = fields.Float(string='')
    sdata28 = fields.Float(string='')
    sdata29 = fields.Float(string='')
    sdata30 = fields.Float(string='')
    sdata31 = fields.Float(string='')
    sdata32 = fields.Float(string='')
    sdata33 = fields.Float(string='')
    sdata34 = fields.Float(string='')
    sdata35 = fields.Float(string='')
    sdata36 = fields.Float(string='')
    sdata37 = fields.Float(string='')
    sdata38 = fields.Float(string='')
    sdata39 = fields.Float(string='')
    sdata40 = fields.Float(string='')
    sdata41 = fields.Float(string='')
    sdata42 = fields.Float(string='')
    sdata43 = fields.Float(string='')
    sdata44 = fields.Float(string='')
    sdata45 = fields.Float(string='')
    sdata46 = fields.Float(string='')
    sdata47 = fields.Float(string='')
    sdata48 = fields.Float(string='')
    sdata49 = fields.Float(string='')
    sdata50 = fields.Float(string='')
    udf = fields.Char()
