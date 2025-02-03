from odoo import field, api, models

class VehicleInfo(models.Model):
    _name = 'vehicle.info'
    _description = 'Vehicle Info'

    owner = field.Char(string='Chủ xe')
    email = field.Char(string='Email')
    total_money = field.Float(string='Doanh thu khách hàng')
    plate_number = field.Integer(string='Biển số xe')
    type = field.Char(string='Loại xe')
    trademark = field.Char(string='Dòng xe')
    model = field.Char(string='Model')
    VIN = field.Char(string='Số khung')
    engine = field.Char(string='Số máy')
    hmv_exp_date = field.Datetime(string='Ngày hết hạn BD HMV')
    guarantee_exp_date = field.Datetime(string='Ngày hết hạn bảo hành')

