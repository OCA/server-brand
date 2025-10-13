# Copyright 2024 level4 (https://level4.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo.tests import common


class TestDisableOdooOnline(common.TransactionCase):
    def test_dummy(self):
        # Necessary for CI, since now the warning of 0 tests executed fails
        # the whole pipeline. In the future if tests are needed for this module
        # they should be implemented here.
        self.assertTrue(True)
