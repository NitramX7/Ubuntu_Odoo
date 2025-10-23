# -*- coding: utf-8 -*-
# from odoo import http


# class MartinModulo(http.Controller):
#     @http.route('/martin_modulo/martin_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/martin_modulo/martin_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('martin_modulo.listing', {
#             'root': '/martin_modulo/martin_modulo',
#             'objects': http.request.env['martin_modulo.martin_modulo'].search([]),
#         })

#     @http.route('/martin_modulo/martin_modulo/objects/<model("martin_modulo.martin_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('martin_modulo.object', {
#             'object': obj
#         })

