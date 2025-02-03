{
    'name': 'Hino_Project',
    'version': '17.0.1.0',
    'author': 'Le Chinh Dai',
    'license': 'LGPL-3',
    'depends': ['base', 'repair', 'appointment', 'fleet'],
    'data': [
        'views/repair_quotations.xml',
        'views/repair_order_view.xml',
        # 'views/repair_order_header_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}