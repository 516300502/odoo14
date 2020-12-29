# -*- coding: utf-8 -*-
# Copyright (c) Open Value All Rights Reserved

{
'name': 'MRP Product Costing',
 'summary': 'MRP Product Costing',
 'version': '13.4.0.0.0',
 'category': 'Manufacturing',
  "website": 'linkedin.com/in/openvalue-consulting-472448176',
  'author': "Open Value",
  'support': 'info.openvalue@gmail.com',
  'license': "Other proprietary",
  'price': 400.00,
  'currency': 'EUR',
    "depends": [
        'stock_account',
        'purchase',
        'mrp',
        'account',
        'analytic',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/wip_amount_views.xml',
        'views/account_move_line_views.xml',
        'views/account_analytic_line_views.xml',
        'views/mrp_product_costing_parameters.xml',
        'views/mrp_workcenter_views.xml',
        'views/mrp_bom_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_product_costing_views.xml',
        'views/mrp_wip_costing_views.xml',

    ],
  'application': False,
  'installable': True,
  'auto_install': False,
  'images': ['static/description/banner.png'],
}
