# Copyright 2020-2023 Onestein (<http://www.onestein.eu>)
# Copyright 2020 Akretion (<http://www.akretion.com>)
# Copyright 2023 Le Filament (https://le-filament.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import json

from lxml import etree

from odoo.tests import common


class TestRemoveOdooEnterprise(common.TransactionCase):
    def test_res_config_settings(self):
        """
        This test case checks the XML architecture of res.config.settings view,
        specifically searching for div elements with a field element where widget
        attribute is 'upgrade_boolean'. If such an element exists, it should have
        the class "d-none".
        """
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])
        # Validate, there are no more visible setting boxes in the view,
        # which include fields with upgrade_boolean widgets
        query_settings_box = (
            "//div[contains(@class, 'o_setting_box')]"
            "[.//field[@widget='upgrade_boolean']]"
        )
        setting_boxes = doc.xpath(query_settings_box) or None
        self.assertIsNone(setting_boxes)
        # Validate, there are no more visible settings containers in the view,
        # which only include hidden setting boxes, and therefore appear empty
        # and check if they are hidden
        query_settings_container = (
            "//div[contains(@class, 'o_settings_container')]"
            "[not(.//div[contains(@class, 'o_setting_box') "
            "and not(contains(@class, 'd-none'))])]"
        )
        settings_container = doc.xpath(query_settings_container) or None
        self.assertIsNone(settings_container)

    def test_hide_empty_containers(self):
        """Test the _hide_empty_containers method"""
        conf = self.env["res.config.settings"].create({})

        # Create a test XML document with empty containers
        xml_content = """
        <form>
            <h2>Heading 1</h2>
            <div class="o_settings_container">
                <div class="o_setting_box d-none">Hidden setting box</div>
            </div>
            <h2>Heading 2</h2>
            <div class="o_settings_container">
                <div class="o_setting_box">Visible setting box</div>
            </div>
            <h2>Heading 3</h2>
            <div class="o_settings_container">
                <div class="o_setting_box d-none">Another hidden setting box</div>
            </div>
        </form>
        """
        doc = etree.XML(xml_content)

        # Apply the method to hide empty containers
        conf._hide_empty_containers(doc)

        # Check that empty containers and their headings are hidden
        empty_containers = doc.xpath("//div[@class='d-none']")
        self.assertEqual(len(empty_containers), 2)

        # Check that headings before empty containers are hidden
        hidden_headings = doc.xpath("//h2[@class='d-none']")
        self.assertEqual(len(hidden_headings), 2)
        self.assertEqual(hidden_headings[0].text, "Heading 1")
        self.assertEqual(hidden_headings[1].text, "Heading 3")

        # Check that containers with visible setting boxes are not hidden
        visible_containers = doc.xpath("//div[@class='o_settings_container']")
        self.assertEqual(len(visible_containers), 1)

    def test_hide_enterprise_settings(self):
        """Test the _hide_enterprise_settings method"""
        conf = self.env["res.config.settings"].create({})

        # Create a test XML document with upgrade_boolean widgets
        xml_content = """
        <form>
            <div class="o_setting_box">
                <div>
                    <field name="show_effect" widget="upgrade_boolean"/>
                </div>
            </div>
            <div class="o_setting_box">
                <div>
                    <field name="field2"/>
                </div>
            </div>
        </form>
        """
        doc = etree.XML(xml_content)

        # Apply the method to hide enterprise settings
        conf._hide_enterprise_settings(doc)

        # Check that setting boxes with upgrade_boolean widgets are hidden
        hidden_boxes = doc.xpath("//div[@class='d-none']")
        self.assertEqual(len(hidden_boxes), 1)

        # Check that other setting boxes are not hidden
        visible_boxes = doc.xpath("//div[@class='o_setting_box']")
        self.assertEqual(len(visible_boxes), 1)

    def test_search_payment_providers(self):
        """
        This function checks if there are any payment providers in the database,
        fetches them using a search query, and then verifies that none of these
        providers have an associated module to buy.
        """
        if self.env.get("payment.provider"):
            acquirer_ids = self.env["payment.provider"].search([])
            self.assertFalse(any([a.module_to_buy for a in acquirer_ids]))

    def test_search_ir_module(self):
        """
        This function is used to test the search method from 'ir.module.module' model.
        It checks if there are any modules without a purchase cost (to_buy = False).
        """
        module_ids = self.env["ir.module.module"].search([])
        self.assertFalse(any([m.to_buy for m in module_ids]))

    def test_appstore_invisible(self):
        """The appstore widget is invisible"""
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])

        query = "//div[@id='appstore']"
        for item in doc.xpath(query):
            invisible_attrib = json.loads(item.attrib["modifiers"])
            self.assertTrue(invisible_attrib["invisible"])

    def test_appstore_visible(self):
        """Disabling the view makes the appstore widget visible again"""
        conf_form_view = self.env.ref(
            "remove_odoo_enterprise.res_config_settings_view_form"
        )
        conf_form_view.active = False
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])

        query = "//div[@id='appstore']"
        for item in doc.xpath(query):
            self.assertNotIn("modifiers", item.attrib)
