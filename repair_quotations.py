from odoo import api, fields, models


class RepairQuotations(models.Model):
    _inherit = 'repair.order'

    # Header fields
    # name = fields.Char(string='Mã phiếu', related='x_quotation_id.name', store=True)
    name = fields.Char(string='Name')
    x_quotation_id = fields.Many2one('repair.order', string='Số báo giá')
    x_vehicle_plate = fields.Many2one('repair.order', string='Biển số')
    x_vin_number = fields.Many2one('repair.order', string='Số khung - VIN')
    x_owner_id = fields.Many2one('repair.order', string='Chủ xe')
    x_repair_date = fields.Datetime(string='Ngày sửa chữa')
    x_completion_date = fields.Datetime(string='Ngày hoàn thành')
    x_job_type_id = fields.Many2one('repair.order', string='Loại công việc')
    x_service_advisor_id = fields.Many2one('repair.order', string='CVDV')
    x_appointment_id = fields.Many2one('repair.order', string='Đặt hẹn')
    x_appointment_status = fields.Many2one('repair.order', string='Trạng thái đặt hẹn')
    status = fields.Selection([
        ('draft', 'Nháp'),
        ('repairing', 'Đang sửa chữa'),
        ('completed', 'Hoàn thành'),
        ('cancel', 'Hủy'),
        ('created', 'Đã tạo YCTT')
    ], string='Trạng thái', default='draft')

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

