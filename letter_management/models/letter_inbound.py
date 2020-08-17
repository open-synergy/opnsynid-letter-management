# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class LetterInbound(models.Model):
    _name = "letter.inbound"
    _inherit = "letter.common"
    _description = "Inbound Letter"

    @api.model
    def _default_direction(self):
        return "inbound"

    direction = fields.Selection(
        default=lambda self: self._default_direction(),
    )
