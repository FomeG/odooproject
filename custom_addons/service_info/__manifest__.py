# -*- coding: utf-8 -*-
{
    'name': "Service Info",
    'summary': "Service Information Management",
    'description': """
        Module for managing service information and work lists in repair orders
    """,
    'author': "Your Company",
    'website': "https://www.yourcompany.com",
    'category': 'Services',
    'version': '17.0.1.0',
    'depends': [
        'base',
        'repair',
        'stock',
        'product',
    ],
    'data': [
        'views/tab_service_info_worklist_service_views.xml',  # Added new view
    ],
    'installable': True,
    'application': False,
}