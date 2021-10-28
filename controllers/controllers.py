# -*- coding: utf-8 -*-
# from odoo import http


# class SaleBurguer(http.Controller):
#     @http.route('/sale_burguer/sale_burguer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_burguer/sale_burguer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_burguer.listing', {
#             'root': '/sale_burguer/sale_burguer',
#             'objects': http.request.env['sale_burguer.sale_burguer'].search([]),
#         })

#     @http.route('/sale_burguer/sale_burguer/objects/<model("sale_burguer.sale_burguer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_burguer.object', {
#             'object': obj
#         })
