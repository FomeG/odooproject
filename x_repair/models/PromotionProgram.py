from odoo import models, fields

class PromotionProgram(models.Model):
    _name = 'promotion.program'
    _description = 'Chương trình khuyến mại'

    name = fields.Char(string="Tên Chương Trình", required=True)
    engine_number = fields.Char(string="Số Máy (Engine)")
    main_road = fields.Char(string="Cung Đường Chính")
    body_type = fields.Selection([
        ('flat', 'Loại Thùng Phẳng'),
        ('box', 'Loại Thùng Hộp'),
        ('tipper', 'Loại Thùng Xả'),
    ], string="Loại Thùng", default='flat')
    body_marker = fields.Char(string="Nơi Làm Thùng (Body Marker)")
    transmission = fields.Selection([
        ('manual', 'Hộp Số Cơ'),
        ('automatic', 'Hộp Số Tự Động'),
    ], string="Hộp Số (Transmission)", default='manual')
    delivery_date = fields.Date(string="Ngày Giao Đại Lý")
    owner_email = fields.Char(string="Email Chủ Xe")
    customer_revenue = fields.Float(string="Doanh Thu Khách Hàng")

