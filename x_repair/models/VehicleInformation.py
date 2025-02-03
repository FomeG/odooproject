from odoo import models, fields

class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _description = 'Vehicle Information'

    # Thông tin về biển số và xe
    plate_number = fields.Char(string='Plate Number', required=True)
    vehicle_type = fields.Selection([
        ('1', 'Hino'),
        ('2', 'Toyota'),
        ('3', 'Ford'),
        # Thêm các lựa chọn khác tùy vào yêu cầu
    ], string='Vehicle Type', default='1', required=True)
    trademark = fields.Many2one('vehicle.trademark', string='Trademark', required=True)
    model = fields.Many2one('vehicle.model', string='Model', required=True)
    vin_number = fields.Char(string='VIN', required=True)
    engine_number = fields.Char(string='Engine', required=True)

    # Ngày hết hạn bảo dưỡng và bảo hành
    hmv_maintenance_expiry = fields.Date(string='HMV Maintenance Expiry Date', required=True)
    warranty_expiry = fields.Date(string='Warranty Expiry Date', required=True)
    
    # Trường này sẽ lưu thông tin từ bảng khác, nếu cần
    # Ví dụ, bạn có thể có bảng "vehicle.trademark" và "vehicle.model" riêng biệt.
