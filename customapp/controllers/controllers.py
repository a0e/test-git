# -*- coding: utf-8 -*-
# from odoo import http


# class Customapp(http.Controller):
#     @http.route('/customapp/customapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customapp/customapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customapp.listing', {
#             'root': '/customapp/customapp',
#             'objects': http.request.env['customapp.customapp'].search([]),
#         })

#     @http.route('/customapp/customapp/objects/<model("customapp.customapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customapp.object', {
#             'object': obj
#         })
