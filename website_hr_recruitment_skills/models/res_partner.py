# -*- coding: utf-8 -*-

from odoo import fields, models

class Partner(models.Model):
    _description = 'Contact'
    _inherit = ['format.address.mixin', 'avatar.mixin']
    _name = "res.partner"

    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
