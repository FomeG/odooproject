{
    'name': "Repair History",
    'summary': "Add repair history tracking to repair orders",
    'description': """
        This module adds repair history tracking functionality to repair orders:
        - Track repair order references
        - Track job types
        - History view in repair orders
    """,
    'author': "Your Company",
    'website': "https://www.yourcompany.com",
    'category': 'Manufacturing/Repair',
    'version': '17.0.1.0',
    'depends': ['base', 'repair'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
}