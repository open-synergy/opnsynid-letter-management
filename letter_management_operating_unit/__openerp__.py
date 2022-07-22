# Copyright 2022 PT. Simetri Sinergi Indonesia
# Copyright 2022 OpenSynergy Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Letter Management with Operating Units",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "operating_unit",
        "letter_management",
    ],
    "data": [
        "security/ir_rule_data.xml",
        "security/res_group_data.xml",
        "views/letter_common_views.xml",
    ],
}
