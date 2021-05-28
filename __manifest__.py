# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'fashion_store',
    'version': '0.1',
    'summary': 'Fashion store topic for exam',
    'description': """This module is for exam purpose
    """,
    'depends': ['base'],
    'data': [
        'views/fashion_garment.xml',
        'views/orderline.xml',
        'views/order.xml'
        #'garment.xml'
       ],
    'installable': True,
    'auto_install': False
}