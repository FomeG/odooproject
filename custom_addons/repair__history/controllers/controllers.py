# -*- coding: utf-8 -*-
# from odoo import http


# class RepairHistory(http.Controller):
#     @http.route('/repair__history/repair__history', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/repair__history/repair__history/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('repair__history.listing', {
#             'root': '/repair__history/repair__history',
#             'objects': http.request.env['repair__history.repair__history'].search([]),
#         })

#     @http.route('/repair__history/repair__history/objects/<model("repair__history.repair__history"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('repair__history.object', {
#             'object': obj
#         })

