from odoo import api, fields, models


class RepairQuotations(models.Model):
    _name = 'repair.quotations'
    _description = 'Repair Quotations'

    # Header fields
    name = fields.Char(string='Name', required=True)
    x_quotation_id = fields.Char(string='Quotation ID')  # Changed from Many2one
    x_vehicle_plate = fields.Char(string='Vehicle Plate')  # Changed from Many2one
    x_vin_number = fields.Char(string='VIN Number')  # Changed from Many2one
    x_owner_id = fields.Many2one('res.partner', string='Owner')  # Changed to res.partner
    x_repair_date = fields.Date(string='Repair Date')  # Changed from Many2one to Date
    x_completion_date = fields.Date(string='Completion Date')  # Changed from Many2one to Date
    x_job_type_id = fields.Selection([
        ('warranty', 'Warranty'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair')
    ], string='Job Type')  # Changed from Many2one to Selection
    x_service_advisor_id = fields.Many2one('res.users', string='Service Advisor')  # Changed to res.users
    x_appointment_id = fields.Char(string='Appointment ID')  # Changed from Many2one
    x_appointment_status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Appointment Status')  # Changed from Many2one to Selection
    status = fields.Selection([
        ('draft', 'Draft'),
        ('repairing', 'Repairing'),
        ('completed', 'Completed'),
        ('cancel', 'Cancelled'),
        ('created', 'Created')
    ], string='Status', default='draft')