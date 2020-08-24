from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'appointment_seq'
    _order = 'appointment_date desc'

    @api.model
    def create(self, vals):
        if vals.get('appointment_seq', _('New') == _('New')):
            vals['appointment_seq'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    appointment_seq = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer(string='Age', related='patient_id.age')
    notes = fields.Text(stirng='Registration Note')
    appointment_date = fields.Date(string='Date', required=True)
