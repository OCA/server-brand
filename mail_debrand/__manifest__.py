# Copyright 2016 Tecnativa - Jairo Llopis
# Copyright 2017 Tecnativa - Pedro M. Baeza
# Copyright 2019 ForgeFlow S.L. - Lois Rilo <lois.rilo@forgeflow.com>
# 2020 NextERP Romania
# Copyright 2021 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail Debrand",
    "summary": """Removes Odoo branding from sent emails
    by deleting the 'Powered by Odoo' link and any mention
    of 'Odoo' in template texts longer than 20 characters.""",
    "version": "18.0.1.0.1",
    "category": "Social Network",
    "website": "https://github.com/OCA/server-brand",
    "author": """Tecnativa, ForgeFlow, Onestein, Sodexis, Nexterp Romania,
             Odoo Community Association (OCA)""",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "development_status": "Production/Stable",
    "maintainers": ["pedrobaeza", "joao-p-marques"],
}
