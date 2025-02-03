from odoo import api, fields, models


class RepairQuotations(models.Model):
    _inherit = 'repair.order'

    #Thông tin header chứng từ - Thông tin chung
    x_customer_feedback = fields.Char(string='Ý kiến khách hàng', help='Ý kiến khách hàng')
    x_notes = fields.Char(string='Notes', help='Ghi chú/Lưu ý/Khuyến nghị')
    x_content = fields.Char(string='Nội dung', help='Nội dung')

    x_pricelist_id = fields.Many2one(
        'product.pricelist',
        string='Bảng giá',
        help='Bảng giá được liên kết')

    x_total = fields.Monetary(string='Thành tiền', help='Thành tiền')
    x_tax_amount = fields.Monetary(string='Tiền thuế', help='Tiền thuế')
    x_total_amount = fields.Monetary(string='Tổng', help='Tổng')

