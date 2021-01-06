# -*- coding: utf-8 -*-
{
    'name': "equipment",

    'summary': """
        设备数据及报表""",

    'description': """
        设备数据及报表
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'report/rang1_test_report_views.xml',
        'report/taidt_test_report_views.xml',
        'report/line_test_report_views.xml',
        'report/c_tbltest_data_report_views.xml',
        'security/ir.model.access.csv',
        'views/c_capacity_test.xml',
        'views/line_test.xml',
        'views/taidt_test.xml',
        'views/rang1_test.xml',
        'views/wentiao_test.xml',
        'views/equipment_menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'images': ['static/description/icon.png'],
}
