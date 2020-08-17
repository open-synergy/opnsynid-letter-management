# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class LetterCommon(models.AbstractModel):
    _name = "letter.common"
    _description = "Abstract Model for Letter"
    _inherit = [
        "mail.thread",
        "base.sequence_document",
        "base.workflow_policy_object",
        "tier.validation",
        "base.cancel.reason_common",
    ]
    _state_from = [
        "draft",
        "confirm",
    ]
    _state_to = [
        "open",
    ]

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    @api.model
    def _default_date(self):
        return fields.Date.today()

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(LetterCommon, self)
        _super._compute_policy()

    name = fields.Char(
        string="Subject",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    number = fields.Char(
        string="# Document",
        required=True,
        default="/",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Letter Type",
        comodel_name="letter.type",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    direction = fields.Selection(
        string="Direction",
        selection=[
            ("inbound", "Inbound"),
            ("outbound", "Outbound"),
        ],
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    digital = fields.Boolean(
        string="Digital",
        default=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    user_id = fields.Many2one(
        string="Responsible",
        comodel_name="res.users",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date = fields.Date(
        string="Letter Date",
        require=True,
        default=lambda self: self._default_date(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    sent_date = fields.Date(
        string="Sent Date",
        require=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    received_date = fields.Date(
        string="Received Date",
        require=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    recipient_partner_id = fields.Many2one(
        string="Recipient Partner",
        comodel_name="res.partner",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    sender_partner_id = fields.Many2one(
        string="Sender Partner",
        comodel_name="res.partner",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    weight = fields.Float(
        string="Weight",
    )
    weight_uom_id = fields.Many2one(
        string="Weight UoM",
        comodel_name="product.uom",
    )
    lenght = fields.Float(
        string="Lenght",
    )
    lenght_uom_id = fields.Many2one(
        string="Lenght UoM",
        comodel_name="product.uom",
    )
    width = fields.Float(
        string="Width",
    )
    width_uom_id = fields.Many2one(
        string="Width UoM",
        comodel_name="product.uom",
    )
    depth = fields.Float(
        string="Depth",
    )
    depth_uom_id = fields.Many2one(
        string="Depth UoM",
        comodel_name="product.uom",
    )
    note = fields.Text(
        string="Note",
    )
    state = fields.Selection(
        string="State",
        required=True,
        readonly=True,
        track_visibility="onchange",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("done", "Done"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        copy=False,
    )
    # Log Fields
    confirm_date = fields.Datetime(
        string="Confirmation Date",
        readonly=True,
        copy=False,
    )
    confirm_user_id = fields.Many2one(
        string="Confirmation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    open_date = fields.Datetime(
        string="Opened Date",
        readonly=True,
        copy=False,
    )
    open_user_id = fields.Many2one(
        string="Open By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    finish_date = fields.Datetime(
        string="Finish Date",
        readonly=True,
        copy=False,
    )
    finish_user_id = fields.Many2one(
        string="Finish By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    cancel_date = fields.Datetime(
        string="Cancellation Date",
        readonly=True,
        copy=False,
    )
    cancel_user_id = fields.Many2one(
        string="Cancellation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    # Policy Fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    done_ok = fields.Boolean(
        string="Can Finish",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    restart_approval_ok = fields.Boolean(
        string="Can Restart Approval",
        compute="_compute_policy",
    )

    @api.multi
    def action_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())
            document.request_validation()

    @api.multi
    def action_approve(self):
        for document in self:
            document.write(document._prepare_approve_data())

    @api.multi
    def action_done(self):
        for document in self:
            document.write(document._prepare_done_data())

    @api.multi
    def action_cancel(self):
        for document in self:
            document.write(document._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())

    @api.multi
    def validate_tier(self):
        _super = super(LetterCommon, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_approve()

    @api.multi
    def restart_validation(self):
        _super = super(LetterCommon, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
            "confirm_user_id": self.env.user.id,
            "confirm_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        result = {
            "state": "open",
        }
        return result

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        result = {
            "state": "done",
            "finish_user_id": self.env.user.id,
            "finish_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
            "cancel_user_id": self.env.user.id,
            "cancel_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "confirm_user_id": False,
            "confirm_date": False,
            "finish_user_id": False,
            "finish_date": False,
            "cancel_user_id": False,
            "cancel_date": False,
        }
        return result

    @api.model
    def create(self, values):
        _super = super(LetterCommon, self)
        result = _super.create(values)
        result.write({
            "number": result._create_sequence(),
        })
        return result

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for document in self:
            if document.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(LetterCommon, self)
        _super.unlink()
