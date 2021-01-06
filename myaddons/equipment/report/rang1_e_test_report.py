# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Rang1_test_report(models.AbstractModel):
    _name = "report.equipment.rang1_e_test"
    _description = '量程压测试报告'



    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sehin.data'].browse(docids)
        doc = docs[0]

        return {
            'docids': docids,
            'docs': docs,
            'report_title': '量程测试报告(英文)'
        }