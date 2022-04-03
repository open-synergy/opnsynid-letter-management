# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import api, fields, models


class LetterOutbound(models.Model):
    _name = "letter.outbound"
    _inherit = "letter.common"
    _description = "Outbound Letter"

    @api.model
    def _default_direction(self):
        return "outbound"

    direction = fields.Selection(
        default=lambda self: self._default_direction(),
    )
