from odoo import models, fields, api

class ChuXe(models.Model):
    _inherit = 'repair.order'

    # header chứng từ chủ xe
    partner_id = fields.Many2one('res.partner', string="Chủ xe")
    x_driver = fields.Char(string="Lái xe")
    x_driver_phone = fields.Char(string="SĐT lái xe")
