from odoo import models, fields, api


class OrderLine(models.Model):
    _name = 'order.line'
    name = fields.Char(string='Name')
    order_date = fields.Date(string=' Order Date')
    quantity = fields.Integer(string='Quantity')
    total = fields.Integer(string='Total')
    price = fields.Integer(string='Price')
    garment_id = fields.Many2one('fashion.garment', string='Garment')
    orderdate_id = fields.Many2one('order.datelist', string='Order Date')
    garment_type = fields.Selection([('t-shirt', 'T-Shirt'),
                                     ('shirt', 'Shrirt'),
                                     ('jeans', 'Jeans'),
                                     ('short', 'Short'),
                                     ('shoe', 'Shoe'),
                                     ])







