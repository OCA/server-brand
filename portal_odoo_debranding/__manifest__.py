# Copyright 2020 Lorenzo Battistini @ TAKOBI
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Remove Odoo Branding from Portal",
    "version": "14.0.1.0.1",
    "development_status": "Beta",
    "category": "Hidden",
    "website": "https://github.com/OCA/server-brand",
    "author": "TAKOBI, Odoo Community Association (OCA), Ilyas, Ooops404, ",
    "maintainers": ["eLBati", "ivantodorovich"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "portal",
    ],
    "data": [
        "views/portal_templates.xml",
    ],
}
