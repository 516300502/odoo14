# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright Domiup (<http://domiup.com>).
#
##############################################################################

from odoo import api, models, fields


class MultiApprovalTypeLine(models.Model):
    _inherit = 'multi.approval.type.line'

    special_user = fields.Selection(
        [('Line Manager', 'Line Manager'),
         ('Coach', 'Coach'),
         ('Manager of Department', 'Manager of Department'),
         ], string="Special User")

    def get_user(self):
        self.ensure_one()
        res = super(MultiApprovalTypeLine, self).get_user()
        if not self.special_user:
            return res
        user = self.env.user  # who is logged in
        if self.special_user == 'Line Manager':
            if user.employee_parent_id and user.employee_parent_id.user_id:
                return user.employee_parent_id.user_id.id
        elif self.special_user == 'Coach':
            if user.coach_id and user.coach_id.user_id:
                return user.coach_id.user_id.id
        elif user.department_id and user.department_id.manager_id and user.department_id.manager_id.user_id:
            return user.department_id.manager_id.user_id.id
        return res
