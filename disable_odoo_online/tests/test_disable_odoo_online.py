# Copyright 2024 level4 (https://level4.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from unittest import mock

from odoo.release import version_info
from odoo.tests import common


class TestDisableOdooOnline(common.TransactionCase):
    def test_apps_menus_moved_to_technical(self):
        technical_parameters = self.env.ref("base.menu_ir_property")
        for xmlid in (
            "base.menu_theme_store",
            "base.menu_third_party",
            "base.menu_module_tree",
        ):
            self.assertEqual(self.env.ref(xmlid).parent_id, technical_parameters)
        self.assertEqual(
            self.env.ref("base.menu_apps").action,
            self.env.ref("base.open_module_tree"),
        )

    def test_update_notification_disabled(self):
        if version_info[5] == "e":
            self.skipTest("The update notifier must stay active on Enterprise")
        Contract = self.env["publisher_warranty.contract"]
        with mock.patch.object(type(Contract), "_get_sys_logs") as get_sys_logs:
            self.assertTrue(Contract.update_notification())
        get_sys_logs.assert_not_called()
