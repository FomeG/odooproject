from odoo import api, fields, models


class RepairQuotations(models.Model):
    _name = 'repair.quotations'
    _description = 'Repair Quotations'

    # Header fields
    name = fields.Char(string='Name', required=True)
    x_quotation_id = fields.Many2one('repair.order', string='Quotation ID')
    x_vehicle_plate = fields.Many2one('repair.order', string='Vehicle Plate')
    x_vin_number = fields.Many2one('repair.order', string='VIN Number')
    x_owner_id = fields.Many2one('repair.order', string='Owner ID')
    x_repair_date = fields.Many2one('repair.order', string='Repair Date')
    x_completion_date = fields.Many2one('repair.order', string='Completion Date')
    x_job_type_id = fields.Many2one('repair.order', string='Job Type')
    x_service_advisor_id = fields.Many2one('repair.order', string='Service Advisor')
    x_appointment_id = fields.Many2one('repair.order', string='Appointment ID')
    x_appointment_status = fields.Many2one('repair.order', string='Appointment Status')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('repairing', 'Repairing'),
        ('completed', 'Completed'),
        ('cancel', 'Cancelled'),
        ('created', 'Created')
    ], string='Status', default='draft')

