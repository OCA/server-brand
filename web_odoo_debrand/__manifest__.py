# Copyright 2025 Milan Topuzov (https://milantopuzov.dev)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Web Debrand (Odoo)",
    "summary": "Hide Odoo branding elements in web backend",
    "version": "19.0.1.0.0",
    "category": "Hidden",
    "website": "https://github.com/OCA/server-brand",
    "author": "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "depends": ["web", "base_setup"],
    "data": [
        "views/res_config_settings_debrand.xml",
        "views/web_layout_debrand.xml",
    ],
    "assets": {},
    "installable": True,
}
