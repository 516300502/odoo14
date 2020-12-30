# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Master Production Schedule',
    'version': '1.0',
    'category': 'Manufacturing/Manufacturing',
    'sequence': 50,
    'summary': '主生产计划',
    'depends': ['mrp', 'purchase_stock'],
    'description': """
                    主生产计划
                    """,
    'data': [
        'security/ir.model.access.csv',
        'security/mrp_mps_security.xml',
        'views/mrp_mps_templates.xml',
        'views/mrp_mps_views.xml',
        'views/mrp_mps_menu_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/mrp_mps_forecast_details_views.xml'
    ],
    'demo': [
        'data/mps_demo.xml',
    ],
    'qweb': [
        "static/src/xml/qweb_templates.xml",
    ],
    'application': True,
}
