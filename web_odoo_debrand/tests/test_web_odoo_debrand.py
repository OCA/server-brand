# Copyright 2025 Milan Topuzov (https://milantopuzov.dev)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from lxml import etree

from odoo.tests import common


class TestWebOdooDebrand(common.TransactionCase):
    def test_settings_about_section_removed(self):
        """The About block in Settings form should be removed."""
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])

        # Ensure the About container is no longer present
        self.assertFalse(
            doc.xpath("//div[@id='about']"),
            "About section container should be removed from Settings form",
        )

        # Also ensure the edition widget from the About block is gone
        self.assertFalse(
            doc.xpath("//widget[@name='res_config_edition']"),
            "Edition widget should be removed with the About section",
        )
