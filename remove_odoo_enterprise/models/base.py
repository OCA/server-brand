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
            # the context key is used for seeing when the call to this method is done
            # from `models.py > fetch` method, bypassing this extra domain in such case
            if self._name == "ir.module.module":
                domain = Domain(domain or []) & Domain([("to_buy", "=", False)])
            elif self._name == "payment.provider":
                domain = Domain(domain or []) & Domain([("module_to_buy", "=", False)])
        return super()._search(domain, *args, **kwargs)
