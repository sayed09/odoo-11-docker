from odoo import api, fields, models, tools, _

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    product_id = fields.Many2One(string='Product')