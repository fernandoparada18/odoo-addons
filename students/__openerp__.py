# -*- coding: utf-8 -*-
{
    'name': "Students Management System",

    'summary': """
        Students Management System""",

    'description': """
Student Management System
=========================
This module will manage details about Students
    """,

    'author': "Fernando Parada",
    'website': "http://fernandoparada.net.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'School Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
