# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Taidt_test_report(models.AbstractModel):
    _name = "report.equipment.taidt_test"
    _description = '片均压测试报告'



    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['fcxrang.siken.data'].browse(docids)
        doc = docs[0]

        return {
            'docids': docids,
            'docs': docs,
            'report_title': '片均压测试报告'
        }