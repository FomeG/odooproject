from odoo import api, fields, models
class TabServiceInfo(models.Model):
    _inherit = 'stock.move'

    #Danh mục phụ tùng (Spare part list)
    product_uom_category_id = fields.Many2one(
        'uom.category', 
        related='product_id.uom_id.category_id',
        string='Product UoM Category',
        store=True,
    )
    default_code = fields.Many2one('product.template', string='Sản phẩm')
    x_product_name = fields.Many2one('product.template', string='Tên sản phẩm')
    product_uom = fields.Many2one('uom.uom', string='ĐVT', required=True)
    product_uom_qty = fields.Float(string='Số lượng', required=True)
    x_pricelist = fields.Many2one('product.pricelist', string='Bảng giá')
    x_unit_price = fields.Float(string='Đơn giá')
    x_hmv_percent = fields.Float(string='% HMV')
    x_dealer_percent = fields.Float(string='% Đại lý')
    x_discount = fields.Float(string='Giảm giá')
    x_tax_excluded = fields.Monetary(string='Thành tiền')
    x_taxes = fields.Many2one('account.tax', string='VAT%')
    x_tax_amount = fields.Float(string='Tiền thuế VAT')