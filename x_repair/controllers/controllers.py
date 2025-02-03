# -*- coding: utf-8 -*-
# from odoo import http


# class XRepair(http.Controller):
#     @http.route('/x_repair/x_repair', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/x_repair/x_repair/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('x_repair.listing', {
#             'root': '/x_repair/x_repair',
#             'objects': http.request.env['x_repair.x_repair'].search([]),
#         })

#     @http.route('/x_repair/x_repair/objects/<model("x_repair.x_repair"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('x_repair.object', {
#             'object': obj
#         })

