# -*- coding: utf-8 -*-
# from odoo import http


# class ServiceInfo(http.Controller):
#     @http.route('/service_info/service_info', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_info/service_info/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_info.listing', {
#             'root': '/service_info/service_info',
#             'objects': http.request.env['service_info.service_info'].search([]),
#         })

#     @http.route('/service_info/service_info/objects/<model("service_info.service_info"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_info.object', {
#             'object': obj
#         })

