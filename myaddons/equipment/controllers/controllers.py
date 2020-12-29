# -*- coding: utf-8 -*-
# from odoo import http


# class Equipment(http.Controller):
#     @http.route('/equipment/equipment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equipment/equipment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('equipment.listing', {
#             'root': '/equipment/equipment',
#             'objects': http.request.env['equipment.equipment'].search([]),
#         })

#     @http.route('/equipment/equipment/objects/<model("equipment.equipment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equipment.object', {
#             'object': obj
#         })
