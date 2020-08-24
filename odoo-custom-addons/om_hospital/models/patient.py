from odoo import models, fields, _, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string="Patient Name", required=True)


class HospitalPatients(models.Model):
    @api.depends('age_group')
    def __compute_age_group(self):
        if self.age:
            if self.age >=18:
                self.age_group = 'major'
            else:
                self.age_group = 'minor'

    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient records'
    _rec_name = 'name'
    name = fields.Char(string='Patient', required=True)
    age = fields.Integer(string='Age', track_visibility='always')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], compute=__compute_age_group)
    notes = fields.Text(string='Registration Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Sequence', required=True, readonly=True, copy=False, index=True,
                           default=lambda self: _('new'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('new')) == _('new'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatients, self).create(vals)
        return result
