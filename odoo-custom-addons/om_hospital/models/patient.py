from odoo import models, fields, _, api


class HospitalPatients(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient records'
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Hospital patient sequence', required=True, readonly=True, copy=False, index=True,
                           default=lambda self: _('new'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('new')) == _('new'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatients, self).create(vals)
        return result