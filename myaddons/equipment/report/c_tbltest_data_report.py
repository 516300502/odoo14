# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Ctbltest_data_report(models.AbstractModel):
    _name = "report.equipment.tbltestdata"
    _description = 'c容量测试报告'



    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['tbltestdata'].browse(docids)
        doc = docs[0]

        return {
            'docids': docids,
            'docs': docs,
            'report_title': 'c容量测试报告'
        }

