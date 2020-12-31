# -*- coding: utf-8 -*-


from odoo import models, fields, api, _



class MrpWorkCenterProductivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'

    setup_duration = fields.Float(_('Setup Duration'))
    teardown_duration = fields.Float(_('Teardown Duration'))
    working_duration = fields.Float(_('Working Duration'))
    overall_duration = fields.Float(_('Overall Duration'))





