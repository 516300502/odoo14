# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import timedelta
from datetime import datetime


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    date_planned_start_wo = fields.Datetime(string="Scheduled Start Date", readonly=True)
    date_planned_finished_wo = fields.Datetime(string="Scheduled End Date", readonly=True)
    date_actual_start_wo = fields.Datetime('Start Date', copy=False, readonly=True, compute="get_actual_dates", store=True)
    date_actual_finished_wo = fields.Datetime('End Date', copy=False, readonly=True, compute="get_actual_dates", store=True)

    def button_plan(self):
        res = super(MrpProduction, self).button_plan()
        for production in self:
            if production.date_start_wo:
                production.date_planned_start_wo = production.date_start_wo
            else:
                production.date_planned_start_wo = datetime.now()
            production.date_planned_finished_wo = False
            planned_date = fields.Datetime.from_string(production.date_planned_start_wo)
            values = {}
            for workorder in production.workorder_ids:
                date_start = planned_date
                time_delta = workorder.duration_expected
                date_end = date_start + timedelta(minutes=time_delta)
                if workorder.workcenter_id.resource_id:
                    calendar = workorder.workcenter_id.resource_calendar_id
                    duration = workorder.duration_expected / 60
                    date_end = calendar.plan_hours(duration, date_start, False, None, None)
                planned_date = date_end
            production.date_planned_finished_wo = fields.Datetime.to_string(planned_date)
        return res

    def button_unplan(self):
        res = super(MrpProduction, self).button_unplan()
        self.write({'date_planned_start_wo': False, 'date_planned_finished_wo': False})
        return True
                    
    @api.depends('state')
    def get_actual_dates(self):
        for record in self:
            record.date_actual_start_wo = False
            record.date_actual_finished_wo = False
            first_wo_id = []
            last_wo_id = []
            if record.workorder_ids:
                if record.state == "done" or record.state == "cost" or record.state == "to_close":
                    first_wo_ids = self.env['mrp.workorder'].search([('production_id', '=', record.id),('state', '=', 'done')])
                    if first_wo_ids:
                        first_wo_id = first_wo_ids[0].id
                        record.date_actual_start_wo = self.env['mrp.workcenter.productivity'].search([('workorder_id', '=', first_wo_id)]).sorted('date_start')[0].date_start
                    last_wo_ids = self.env['mrp.workorder'].search([('production_id', '=', record.id),('state', '=', 'done')])
                    if last_wo_ids:
                        last_wo_id = last_wo_ids[-1].id
                        record.date_actual_finished_wo = self.env['mrp.workcenter.productivity'].search([('workorder_id', '=', last_wo_id)]).sorted('date_end')[-1].date_end
            else:
                if record.state == "confirmed":
                    record.date_actual_start_wo = datetime.now()
                if record.state == "done":
                    record.date_actual_finished_wo = datetime.now()
        return True
