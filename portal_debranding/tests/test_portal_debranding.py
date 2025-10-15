"""Portal debranding tests.

Validates that this module removes Odoo branding from portal pages.
"""

# Copyright 2024 level4 (https://level4.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestPortalOdooDebranding(common.TransactionCase):
    def test_brand_promotion_hidden(self):
        """web.brand_promotion should render nothing after debranding.

        The view sets t-if="False" on the .o_brand_promotion container,
        so the whole block must be skipped at render time.
        """
        html = self.env["ir.ui.view"]._render_template("web.brand_promotion", values={})
        self.assertEqual(html.strip(), "", "Brand promotion block should be removed")

    def test_portal_record_sidebar_no_powered_by(self):
        """The 'Powered by Odoo' notice in portal sidebar must be removed."""
        html = self.env["ir.ui.view"]._render_template(
            "portal.portal_record_sidebar", values={"classes": ""}
        )
        self.assertNotIn("Powered by", html)
        self.assertNotIn("odoo.com?utm_medium=portal", html)
