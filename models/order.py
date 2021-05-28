from odoo import models, fields, api


class Order(models.Model):
    _name = 'order.datelist'
    order_date = fields.Date(string=' Order Date:')
    orderline_ids = fields.One2many("order.line", "orderdate_id", string="Ordered Date")
    quantity = fields.Float(string='Quantity')
    price = fields.Integer(string='Price')
    total = fields.Integer(string='Total')
    tailor_id = fields.Many2one("garment.tailor", string="Tailor")

class GarmentTailor(models.Model):
    _name = "garment.tailor"
    name= fields.Char(string= "Name")
    order_ids = fields.One2many("order.datelist","tailor_id",string="Order list")




