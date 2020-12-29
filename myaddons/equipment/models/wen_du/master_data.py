# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 14:00 PM
@Author  : yuanlixiang
@description: 温调，(主数据)マスタデータ
"""
from odoo import models, fields, api


class Master_Data(models.Model):
    _name = 'master.data'
    _description = '主数据'

    rngno = fields.Integer(string='微波炉号码') #レンジ番号
    master11 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   0% -1
    master12 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   25% -1
    master13 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   50% -1
    master14 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   75% -1
    master15 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   100% -1
    writeday1 = fields.Date(string='登录日1')
    master21 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   0% -1
    master22 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   25% -1
    master23 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   50% -1
    master24 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   75% -1
    master25 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   100% -1
    writeday2 = fields.Date(string='登录日2')
    master31 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   0% -1
    master32 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   25% -1
    master33 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   50% -1
    master34 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   75% -1
    master35 = fields.Float(string='') #ﾏｽﾀﾃﾞｰﾀ   100% -1
    writeday3 = fields.Date(string='登录日3')
