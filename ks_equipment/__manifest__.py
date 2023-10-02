# -*- coding: utf-8 -*-
{
    'name': "ks_equipment",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       Nom projet : Kasia
       Version : Odoo v15 Community Edition 
       Description : Rédaction spécification fonctionnelle
    """,

    'author': "Jules Andrinirina",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr','product','resource','base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_attribution_views.xml',
        'views/templates.xml',
        'report/report_discharge.xml',
        'report/report_attestation.xml',
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
    'application': True,
    'installable': True,

}
