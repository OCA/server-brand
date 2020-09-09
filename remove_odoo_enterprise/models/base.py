# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def search(self, domain, offset=0, limit=None, order=None, count=False):
        res = super().search(domain, offset, limit, order, count)
        if self._name == "payment.acquirer":
            buy_modules = self.env['ir.module.module'].sudo().search([('to_buy', '=', True)])
            domain += [("module_id", "not in", buy_modules.ids)]
        return super().search(domain, offset, limit, order, count)
