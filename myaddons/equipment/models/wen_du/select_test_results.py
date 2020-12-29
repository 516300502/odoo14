# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 14:00 PM
@Author  : yuanlixiang
@description: 温调，(选择实验结果)試験結果選択
"""
from odoo import models, fields, api


class Select_Test_Results(models.Model):
    _name = 'select.test.results'
    _description = '选择实验结果'

    results = fields.Char(string='选择实验结果')  # 印刷画面で試験結果毎に印刷する為の選択項目。下記の試験条件をセットする。
    condition1 = fields.Selection([('0', '未检测'),
                                   ('1', '合格品'),
                                   ('2', '不合格品'),
                                   ], string='实验条件1')  # 試験結果印刷クエリーで検索する条件 ０＝未試験、１＝合格品、２＝不合格品
    condition2 = fields.Selection([('0', '未检测'),
                                   ('1', '合格品'),
                                   ('2', '不合格品'),
                                   ], string='实验条件2')  # 試験結果印刷クエリーで検索する条件 ０＝未試験、１＝合格品、２＝不合格品
    condition3 = fields.Selection([('0', '未检测'),
                                   ('1', '合格品'),
                                   ('2', '不合格品'),
                                   ], string='实验条件3')  # 試験結果印刷クエリーで検索する条件 ０＝未試験、１＝合格品、２＝不合格品
    condition = fields.Selection([('0', '未检测'),
                                  ('1', '合格品'),
                                  ('2', '不合格品'),
                                  ('3', '无'),
                                  ], string='实验条件3')  # 試験結果印刷クエリーで検索する条件 ０＝未試験、１＝合格品、２＝不合格品
