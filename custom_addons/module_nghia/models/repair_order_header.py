# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class RepairOrderInherit(models.Model):
    _inherit = 'repair.order'


    # Override name field to make it required and readonly
    name = fields.Char('Repair Reference', required=True, readonly=True, default='/')



    # Repair Type
    x_repair_type = fields.Selection([
        ('warranty', 'Warranty repairs'),
        ('free_maintenance', 'Free maintenance'),
        ('normal_maintenance', 'Normal maintenance'), 
        ('free_inspection', 'Free inspection'),
        ('spare_part', 'Spare part sales'),
        ('pdi', 'PDI')
    ], string='Loại sửa chữa', required=True)

    # Appointment - using calendar.event instead of appointment.appointment
    x_schedule_id = fields.Many2one('calendar.event', string='Lịch hẹn')

    # CPUS Status 
    x_cpus_status = fields.Selection([
        ('cpus', 'CPUS'),
        ('non_cpus', 'Non CPUS')
    ], string='CPUS')

    # Repair Action
    x_repair_action = fields.Selection([
        ('new', 'Sửa mới'),
        ('redo', 'Sửa lại')
    ], string='Sửa')

    # Repair Result
    x_repair_result = fields.Selection([
        ('pass', 'Sửa đạt yêu cầu'),
        ('pass_with_warning', 'Sửa đạt khuyến cáo'),
        ('fail', 'Không đạt')
    ], string='Kết quả')

    # Service Advisor
    x_service_advisor_id = fields.Many2one('res.users', string='Cố vấn dịch vụ', 
        default=lambda self: self.env.user)

    # Times
    x_entry_time = fields.Datetime('Giờ vào trạm')
    x_reception_time = fields.Datetime('Giờ tiếp nhận')
    x_expected_completion_time = fields.Datetime('Giờ dự kiến hoàn thành')
    x_completion_time = fields.Datetime('Giờ hoàn thành', readonly=True)

    # KM at repair
    x_km_at_repair = fields.Float('Km lúc sửa chữa')

    # Execution Location
    x_execution_location = fields.Selection([
        ('outside', 'Ngoài trạm'),
        ('inside', 'Trong trạm')
    ], string='Nơi thực hiện', default='inside')

    @api.model
    def create(self, vals):
        return super(RepairOrderInherit, self).create(vals)

    def write(self, vals):
        if vals.get('state') == 'done':
            vals['x_completion_time'] = fields.Datetime.now()
            if not (self.x_cpus_status and self.x_repair_action and self.x_repair_result):
                raise ValidationError(_("CPUS Status, Repair Action and Repair Result are required to complete repair"))
        return super(RepairOrderInherit, self).write(vals)