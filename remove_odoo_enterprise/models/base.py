from odoo import models


class Base(models.AbstractModel):
    _inherit = "base"

    def search(self, domain, offset=0, limit=None, order=None, count=False):
        if self._name == "payment.acquirer":
            domain += [("module_to_buy", "=", False)]
        return super().search(domain, offset, limit, order, count)
