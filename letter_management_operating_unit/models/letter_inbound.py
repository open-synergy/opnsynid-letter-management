# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class LetterInbound(models.Model):
    _name = "letter.inbound"
    _description = "Inbound Letter"
    _inherit = [
        "letter.inbound",
        "letter.common",
    ]
