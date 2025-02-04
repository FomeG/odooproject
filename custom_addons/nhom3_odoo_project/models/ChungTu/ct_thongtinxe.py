from odoo import api, fields, models


class ThongTinXe(models.Model):
    _inherit = 'repair.order'

    # Vehicle Information
    x_vehicle_plate = fields.Many2one('fleet.vehicle', string='Biển số xe', required=True,
                                    help='Biển số xe từ thông tin xe')
    x_vehicle_type = fields.Selection([
        ('hino', 'Hino'),
        # Add other types as needed
    ], string='Loại xe', required=True, default='hino')
    
    x_trademark = fields.Many2one('fleet.vehicle.model.brand', string='Dòng xe', required=True,
                                help='Tên xe từ thông tin xe')
    
    x_vehicle_model = fields.Many2one('fleet.vehicle.model', string='Model', required=True,
                                    help='Mẫu xe từ thông tin xe')
    x_vin_number = fields.Many2one('fleet.vehicle', string='Số khung', required=True,
                                  help='Số khung từ thông tin xe')
    
    x_engine_number = fields.Many2one('fleet.vehicle', string='Số máy', required=True,
                                    help='Số máy từ thông tin xe')
    
    x_hmv_maintenance_expiry = fields.Date(string='Ngày hết hạn BD HMV', required=True,
                                         help='Ngày hết hạn từ phiếu đăng ký bảo hành')
    
    x_warranty_expiry = fields.Date(string='Ngày hết hạn bảo hành', required=True,
                                  help='Ngày hết hạn bảo hành từ thông tin xe')

    @api.onchange('x_vin_number')
    def _onchange_vin_number(self):
        if self.x_vin_number:
            vehicle = self.x_vin_number
            self.x_vehicle_plate = vehicle.id
            self.x_trademark = vehicle.brand_id.id
            self.x_vehicle_model = vehicle.model_id.id
            self.x_engine_number = vehicle.id
            self.x_warranty_expiry = vehicle.warranty_expiry_date
