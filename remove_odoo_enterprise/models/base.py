# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# Copyright 2023 Le Filament (https://le-filament.com)
# Copyright 2026 Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.osv import expression
from odoo.tools import Query


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None) -> Query:
        # Don't search modules to buy in modules and payment providers
        if self.env.context.get("active_test", True):
            # the context key is used for seeing when the call to this method is done
            # from `models.py > fetch` method, bypassing this extra domain in such case
            if self._name == "ir.module.module":
                domain = expression.AND([domain or [], [("to_buy", "=", False)]])
            elif self._name == "payment.provider":
                domain = expression.AND([domain or [], [("module_to_buy", "=", False)]])
        return super()._search(domain, offset=offset, limit=limit, order=order)
