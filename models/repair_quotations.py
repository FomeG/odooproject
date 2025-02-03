from odoo import api, fields, models


class RepairQuotations(models.Model):
    _name = 'repair.quotations'
    _description = 'Repair Quotations'

    #Thông tin header chứng từ - Thông tin chung
    x_customer_feedback = fields.Char(string='Customer Feedback', help='Ý kiến khách hàng')
    x_notes = fields.Char(string='Notes', help='Ghi chú/Lưu ý/Khuyến nghị')
    x_content = fields.Char(string='Content', help='Nội dung')

    x_pricelist_id = fields.Many2one(
        'product.pricelist',
        string='Price List',
        help='Bảng giá được liên kết')

    x_total = fields.Monetary(string='Total', help='Thành tiền')
    x_tax_amount = fields.Monetary(string='Tax Amount', help='Tiền thuế')
    x_total_amount = fields.Monetary(string='Total Amount', help='Tổng')

