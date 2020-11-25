# Copyright 2020 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestRemoveOdooEnterprise(common.TransactionCase):
    def test_01(self):
        conf = self.env["res.config.settings"].create({})
        view = conf.fields_view_get(view_type="form")
        view_arch = view["arch"]
        contains_appstore = "upgrade_boolean" in view_arch
        self.assertFalse(contains_appstore)
