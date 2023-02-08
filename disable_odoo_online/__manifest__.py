# Copyright (C) 2013 Therp BV (<http://therp.nl>).
# Copyright (C) 2022 XCG Consulting (<https://xcg-consulting.fr/>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Remove odoo.com Bindings",
    "version": "16.0.1.0.0",
    "author": "Therp BV,GRAP,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-brand",
    "license": "AGPL-3",
    "category": "Hidden",
    "depends": ["mail"],
    "data": ["views/ir_ui_menu.xml"],
    "assets": {
        "web.assets_backend": [
            "disable_odoo_online/static/src/js/user_menu_items.esm.js"
        ],
    },
    "installable": True,
}
