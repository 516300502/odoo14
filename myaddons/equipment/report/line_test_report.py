# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Line_test_report(models.AbstractModel):
    _name = "report.equipment.line_test"
    _description = '直线测试报告'



    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['siken.data'].browse(docids)
        doc = docs[0]


        return {
            'docids': docids,
            'docs': docs,
            'report_title': '直线测试报告'
        }