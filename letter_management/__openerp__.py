# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Letter Management",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "base_sequence_configurator",
        "base_workflow_policy",
        "base_cancel_reason",
        "base_print_policy",
        "base_multiple_approval",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        "menu.xml",
        "views/letter_type_views.xml",
        "views/letter_common_views.xml",
        "views/letter_inbound_views.xml",
        "views/letter_outbound_views.xml",
    ],
}
