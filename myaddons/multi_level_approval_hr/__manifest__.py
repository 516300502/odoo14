# -*- coding: utf-8 -*-
{
    'name': 'Odoo Approval: HR Extension',
    'version': '14.0.1.0',
    'category': 'Approvals',
    'description': """
    You can set the special approver as Line manager, Coach, Manager of the department
    """,
    'summary': '''
    You can set the special approver as Line manager, Coach, Manager of the department
    ''',
    'live_test_url': 'https://demo14.domiup.com',
    'author': 'Domiup',
    'license': 'OPL-1',
    'support': 'domiup.contact@gmail.com',
    'website': 'https://apps.domiup.com/slides/odoo-approval-all-in-one-1',
    'depends': [
        'multi_level_approval',
        'hr'
    ],
    'data': [
        'views/multi_approval_type_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'test': [],
    'demo': [],
    'installable': True,
    'active': False,
    'application': True,
}
