from odoo import models


class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    def search(self, domain, offset=0, limit=None, order=None, count=False):
        domain += [("to_buy", "=", False)]
        return super().search(domain, offset, limit, order, count)
