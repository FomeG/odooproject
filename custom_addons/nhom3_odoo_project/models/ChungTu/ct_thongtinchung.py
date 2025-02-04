from odoo import api, fields, models

class CtThongTinChung(models.Model):
    _inherit = 'repair.order'

    # Fields for currency
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id
    )

    # Thông tin header chứng từ - Thông tin chung
    x_customer_feedback = fields.Char(
        string='Ý kiến khách hàng',
        help='Ý kiến khách hàng'
    )
    x_notes = fields.Char(
        string='Notes',
        help='Ghi chú/Lưu ý/Khuyến nghị'
    )
    x_content = fields.Char(
        string='Nội dung',
        help='Nội dung'
    )

    x_pricelist_id = fields.Many2one(
        'product.pricelist',
        string='Bảng giá',
        help='Bảng giá được liên kết'
    )

    # Monetary fields with currency_field specified
    x_total = fields.Monetary(
        string='Thành tiền',
        help='Thành tiền',
        currency_field='currency_id'
    )
    x_tax_amount = fields.Monetary(
        string='Tiền thuế',
        help='Tiền thuế',
        currency_field='currency_id'
    )
    x_total_amount = fields.Monetary(
        string='Tổng',
        help='Tổng',
        currency_field='currency_id'
    )



    def action_contact(self):
        return

    def action_order_quotations(self):
        return

    def action_export_inv(self):
        return

    def action_customer_care(self):
        return

    def action_feedback(self):
        return

    def action_checkout(self):
        return