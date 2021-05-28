from odoo import models, fields, api


class FashionGarment(models.Model):
    _name = 'fashion.garment'
    entry = fields.Char(string='Entry Name')
    quantity = fields.Integer(string='quantity')
    price = fields.Integer(string='Price')
    garment_type = fields.Selection([('t-shirt', 'T-Shirt'),
                                     ('shirt', 'Shrirt'),
                                     ('jeans', 'Jeans'),
                                     ('short', 'Short'),
                                     ('shoe', 'Shoe'),
                                     ])
    brand = fields.Selection([('nike', 'Nike'),
                              ('levis', 'Levis'),
                              ('adidas', 'Adidas'),
                              ('wrogn', 'Wrogn'),
                              ('pepe', 'Pepe'),
                              ])
