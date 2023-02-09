# Copyright 2020 Onestein (<http://www.onestein.eu>)
# Copyright 2020 Akretion (<http://www.akretion.com>)
# Copyright 2023 Le Filament (https://le-filament.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo.tests import common


class TestRemoveOdooEnterprise(common.TransactionCase):
    def test_res_config_settings(self):
        conf = self.env["res.config.settings"].create({})
        view = conf.get_views([[False, "form"]])["views"]["form"]
        doc = etree.XML(view["arch"])

        query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(query):
            self.assertEqual(item.attrib["class"], "d-none")

    def test_search_base(self):
        if self.env.get("payment.provider"):
            acquirer_ids = self.env["payment.provider"].search([])
            self.assertFalse(any([a.module_to_buy for a in acquirer_ids]))

    def test_search_ir_module(self):
        module_ids = self.env["ir.module.module"].search([])
        self.assertFalse(any([m.to_buy for m in module_ids]))
