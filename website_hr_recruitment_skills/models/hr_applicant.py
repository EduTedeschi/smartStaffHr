# -*- coding: utf-8 -*-

from odoo import models, fields, _
from odoo.exceptions import UserError


class Applicant(models.Model):

    _inherit = 'hr.applicant'

    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=lambda self: self.env.company.country_id)
    country_code = fields.Char(related='country_id.code', string="Country Code")

    def website_form_input_filter(self, request, values):
        super().website_form_input_filter(request, values)
        if 'skill_ids' in request.params:
            values.update({'applicant_skill_ids': [(0, 0, {'skill_type_id': 1, 'skill_id': int(x), 'skill_level_id': 4}) for x in request.params['skill_ids'].split(',')]})
        return values

