# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 15:00 PM
@Author  : yuanlixiang
@description: 温调，(规格值)規格値
"""
from odoo import models, fields, api


class Standard_Value(models.Model):
    _name = 'standard.value'
    _description = '规格值'

    tblno = fields.Integer(string='表格编号') #テーブル番号
    zero_change20 = fields.Float(string='规格值零变动误差20℃') #規格値 ゼロ変動誤差 20℃
    linear_error20 = fields.Float(string='规格值线性误差(正压、负压共用)20℃') #規格値 リニア誤差（正圧、負圧共用） 20℃
    negative_pressure20 = fields.Float(string='负压20') #負圧スパン差20
    changes_total20 =fields.Float(string='总变动误差20℃') #トータル変動誤差 20℃
    zero_change50 = fields.Float(string='规格值零变动误差50℃') #規格値 ゼロ変動誤差 50℃
    linear_error50 = fields.Float(string='规格值线性误差(正压、负压共用)50℃')  # 規格値 リニア誤差（正圧、負圧共用） 50℃
    negative_pressure50 = fields.Float(string='负压50') #負圧スパン差50
    changes_total50 =fields.Float(string='总变动误差50℃') #トータル変動誤差 50℃
    zero_change85 = fields.Float(string='规格值零变动误差85℃') #規格値 ゼロ変動誤差 85℃
    linear_error85 = fields.Float(string='规格值线性误差(正压、负压共用)85℃')  # 規格値 リニア誤差（正圧、負圧共用） 85℃
    negative_pressure85 = fields.Float(string='负压85') #負圧スパン差85
    changes_total85 =fields.Float(string='总变动误差85℃') #トータル変動誤差 85℃
    zero_change10 = fields.Float(string='规格值零变动误差-10℃') #規格値 ゼロ変動誤差 10℃
    linear_error10 = fields.Float(string='规格值线性误差(正压、负压共用)-10℃') #規格値 リニア誤差（正圧、負圧共用） 10℃
    negative_pressure10 = fields.Float(string='负压-10') #負圧スパン差 -10
    changes_total10 =fields.Float(string='总变动误差-10℃') #トータル変動誤差 -10℃
    zero_change30 = fields.Float(string='规格值零变动误差-30℃') #規格値 ゼロ変動誤差 -10℃
    linear_error30 = fields.Float(string='规格值线性误差(正压、负压共用)-30℃') #規格値 リニア誤差（正圧、負圧共用） -10℃
    negative_pressure30 = fields.Float(string='负压-30') #負圧スパン差 -10
    changes_total30 =fields.Float(string='总变动误差-30℃') #トータル変動誤差 -10℃
    zero_change201 = fields.Float(string='规格值零变动误差返回20℃') #規格値 ゼロ変動誤差 戻り20℃
    linear_error201 = fields.Float(string='正压、共压20℃') #規格値 リニア誤差（正圧、負圧共用） 戻り20℃
    negative_pressure201 = fields.Float(string='标准值负压跨度差返回20℃') #規格値 負圧スパン差 戻り20℃
    changes_total201 =fields.Float(string='规格值总变动误差返回20℃') #規格値 トータル変動誤差 戻り20℃



