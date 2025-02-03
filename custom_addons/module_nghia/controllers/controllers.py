# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleNghia(http.Controller):
#     @http.route('/module_nghia/module_nghia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_nghia/module_nghia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_nghia.listing', {
#             'root': '/module_nghia/module_nghia',
#             'objects': http.request.env['module_nghia.module_nghia'].search([]),
#         })

#     @http.route('/module_nghia/module_nghia/objects/<model("module_nghia.module_nghia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_nghia.object', {
#             'object': obj
#         })

