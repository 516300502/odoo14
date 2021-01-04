# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright Domiup (<http://domiup.com>).
#
##############################################################################

from odoo import api, SUPERUSER_ID, _


def migrate(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        approvals = env['multi.approval'].search([])
        for a in approvals:
            seq_date = a.request_date
            code = env['ir.sequence'].next_by_code(
                'multi.approval', sequence_date=seq_date) or _('New')
            a.code = code
