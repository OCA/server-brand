# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# Copyright 2023 Le Filament (https://le-filament.com)
# Copyright 2026 Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.fields import Domain


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _search(self, domain, *args, **kwargs):
        # Don't search modules to buy in modules and payment providers
        if kwargs.get("active_test", True):
            # `fetch()` checks access with `_search([("id", "in", ids)],
            # active_test=False)`: don't hide those records there, or reading a
            # known enterprise module (e.g. res.config.settings) fails
            if self._name == "ir.module.module":
                domain = Domain(domain or []) & Domain([("to_buy", "=", False)])
            elif self._name == "payment.provider":
                domain = Domain(domain or []) & Domain([("module_to_buy", "=", False)])
        return super()._search(domain, *args, **kwargs)
