# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class LetterType(models.Model):
    _name = "letter.type"
    _description = "Letter Type"

    name = fields.Char(
        string="Letter Type",
        required=True
    )
    code = fields.Char(
        string="Code",
    )
    note = fields.Text(
        string="Note"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
    inbound_sequence_id = fields.Many2one(
        string="Inbound Sequence",
        comodel_name="ir.sequence",
        company_dependent=True,
    )
    inbound_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Inbound Letter",
        comodel_name="res.groups",
        relation="rel_inbound_letter_confirm_group",
        column1="type_id",
        column2="group_id",
    )
    inbound_finish_grp_ids = fields.Many2many(
        string="Allow To Finish Inbound Letter",
        comodel_name="res.groups",
        relation="rel_inbound_letter_finish_group",
        column1="type_id",
        column2="group_id",
    )
    inbound_cancel_grp_ids = fields.Many2many(
        string="Allow To Cancel Inbound Letter",
        comodel_name="res.groups",
        relation="rel_inbound_letter_cancel_group",
        column1="type_id",
        column2="group_id",
    )
    inbound_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Inbound Letter",
        comodel_name="res.groups",
        relation="rel_inbound_letter_restart_group",
        column1="type_id",
        column2="group_id",
    )
    inbound_restart_validation_grp_ids = fields.Many2many(
        string="Allow To Restart Validation Inbound Letter",
        comodel_name="res.groups",
        relation="rel_inbound_letter_restart_validation_group",
        column1="type_id",
        column2="group_id",
    )
    outbound_sequence_id = fields.Many2one(
        string="Outbound Sequence",
        comodel_name="ir.sequence",
        company_dependent=True,
    )
    outbound_confirm_grp_ids = fields.Many2many(
        string="Allow To Confirm Outbound Letter",
        comodel_name="res.groups",
        relation="rel_outbound_letter_confirm_group",
        column1="type_id",
        column2="group_id",
    )
    outbound_finish_grp_ids = fields.Many2many(
        string="Allow To Finish Outbound Letter",
        comodel_name="res.groups",
        relation="rel_outbound_letter_finish_group",
        column1="type_id",
        column2="group_id",
    )
    outbound_cancel_grp_ids = fields.Many2many(
        string="Allow To Cancel Outbound Letter",
        comodel_name="res.groups",
        relation="rel_outbound_letter_cancel_group",
        column1="type_id",
        column2="group_id",
    )
    outbound_restart_grp_ids = fields.Many2many(
        string="Allow To Restart Outbound Letter",
        comodel_name="res.groups",
        relation="rel_outbound_letter_restart_group",
        column1="type_id",
        column2="group_id",
    )
    outbound_restart_validation_grp_ids = fields.Many2many(
        string="Allow To Restart Validation Outbound Letter",
        comodel_name="res.groups",
        relation="rel_outbound_letter_restart_validation_group",
        column1="type_id",
        column2="group_id",
    )
