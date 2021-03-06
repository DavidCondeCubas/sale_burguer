# -*- coding: utf-8 -*-
{
    'name': "sale_burguer",

    'summary': """
       Add options of burguer store""",

    'description': """
       Module create to add new fields in sales referents to burguer store.
    """,

    'author': "David Conde Cubas",
    'website': "https://github.com/dcconde",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # Views
        'views/inherited/product_views.xml',
        'views/extra_image_views.xml',

        # Reports
        'reports/sale_burguer_report.xml',
        'reports/template_sale_burguer_report.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
