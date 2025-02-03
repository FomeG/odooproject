# models/repair_order.py
from odoo import models, fields

class RepairOrderExtended(models.Model):
    _inherit = 'repair.order'
    # Trường mặc định của Repair Order
    name = fields.Char(string="Mã phiếu", required=True)
    # Quotation ID (Many2one: Quotation liên kết với Repair Order)
    x_quotation_id = fields.Many2one('sale.order', string="Quotation ID", required=True)
    
    # Vehicle Plate (Many2one: Biển số xe liên kết với Thông tin xe)
    x_vehicle_plate = fields.Many2one('fleet.vehicle', string="Vehicle Plate", required=True)
    
    # VIN Number (Many2one: Số khung - VIN liên kết với Thông tin xe)
    x_vin_number = fields.Many2one('fleet.vehicle', string="VIN Number", required=True)
    
    # Owner (Many2one: Chủ xe liên kết với Thông tin xe)
    x_owner_id = fields.Many2one('res.partner', string="Owner", required=True)
    
    # Repair Date (Datetime: Ngày sửa chữa)
    x_repair_date = fields.Datetime('Repair Date', required=True)
    
    # Completion Date (Datetime: Ngày hoàn thành)
    x_completion_date = fields.Datetime('Completion Date', required=True)
    
    # Job Type (Many2one: Loại công việc)
    x_job_type_id = fields.Many2one('repair.job.type', string="Job Type", required=True)
    
    # Service Advisor (Many2one: Cố vấn dịch vụ)
    x_service_advisor_id = fields.Many2one('res.users', string="Service Advisor", required=True)
    
    # Appointment ID (Many2one: Đặt hẹn liên kết với Repair Order)
    x_appointment_id = fields.Many2one('repair.appointment', string="Appointment ID", required=True)
    
    # Appointment Status (Many2one: Trạng thái đặt hẹn)
    x_appointment_status = fields.Many2one('repair.appointment.status', string="Appointment Status", required=True)
    
    # Status (Selection: Trạng thái sửa chữa)
    status = fields.Selection([
        ('draft', 'Nháp'),
        ('repairing', 'Đang sửa chữa'),
        ('completed', 'Hoàn thành'),
        ('cancelled', 'Huỷ'),
        ('sent_for_approval', 'Đã tạo YCTT')
    ], string='Status', default='draft', required=True)
