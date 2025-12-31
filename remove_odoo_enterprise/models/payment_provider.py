# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# Copyright 2023 Le Filament (https://le-filament.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


# class PaymentProvider(models.Model):
#    _inherit = "payment.provider"
#
#    @api.model
#    def search_fetch(self, domain, field_names, offset=0, limit=None, order=None):
#        res = super().search_fetch(domain, field_names, offset, limit, order)
#        return res.filtered(lambda a: not a.module_to_buy)
#
#    @api.model
#    def search(self, domain, offset=0, limit=None, order=None):
#        res = super().search(domain, offset=offset, limit=limit, order=order)
#        return res.filtered(lambda a: not a.module_to_buy)