# -*- coding: utf-8 -*-
"""
@Time    : 12/24/2020 10:00 PM
@Author  : yuanlixiang
@description: 温调，(稳定时间)安定時間
"""
from odoo import models, fields, api


class Stabilization_Time(models.Model):
    _name = 'stabilization.time'
    _description = '稳定时间'


    rngno = fields.Integer(string='微波炉号码') #レンジ番号
    waittim1 = fields.Integer(string='压力稳定时间0%') #圧力安定時間 0%
    waittim2 = fields.Integer(string='压力稳定时间25%') #圧力安定時間 25%
    waittim3 = fields.Integer(string='压力稳定时间50%') #圧力安定時間 50%
    waittim4 = fields.Integer(string='压力稳定时间75%') #圧力安定時間 75%
    waittim5 = fields.Integer(string='压力稳定时间100%') #圧力安定時間 100%








