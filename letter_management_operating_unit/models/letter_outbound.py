# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class LetterOutbound(models.Model):
    _name = "letter.outbound"
    _description = "Outbound Letter"
    _inherit = [
        "letter.outbound",
        "letter.common",
    ]
