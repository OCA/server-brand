# Copyright 2025 Milan Topuzov (https://milantopuzov.dev)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from lxml import etree

from odoo.tests import common


class TestWebDebranding(common.TransactionCase):
    def test_settings_about_section_hidden(self):
        """The About block in Settings form should be hidden."""
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])

        about_nodes = doc.xpath("//div[@id='about']")
        self.assertTrue(about_nodes, "About section container should exist in the view")
        self.assertIn(
            "invisible",
            about_nodes[0].attrib,
            "About section should be hidden via invisible='1'",
        )
