# Copyright 2020 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestRemoveOdooAppstore(common.TransactionCase):
    def test_01(self):
        conf = self.env["res.config.settings"].create({})
        view = conf.fields_view_get(view_type="form")
        view_arch = view["arch"]
        if isinstance(view_arch, bytes):
            view_arch = view_arch.decode("utf-8")
        contains_appstore = "appstore" in view_arch
        self.assertFalse(contains_appstore)

    def test_02(self):
        conf_form_view = self.env.ref(
            "remove_odoo_mobile_appstore.res_config_settings_view_form"
        )
        conf_form_view.active = False
        conf = self.env["res.config.settings"].create({})
        view = conf.fields_view_get(view_type="form")
        view_arch = view["arch"]
        if isinstance(view_arch, bytes):
            view_arch = view_arch.decode("utf-8")
        contains_appstore = "appstore" in view_arch
        self.assertTrue(contains_appstore)
