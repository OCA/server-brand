# Copyright (C) 2013 Therp BV (<http://therp.nl>).
# Copyright (C) 2022 XCG Consulting (<https://xcg-consulting.fr/>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models
from odoo.release import version_info


class PublisherWarrantyContract(models.AbstractModel):
    _inherit = "publisher_warranty.contract"

    def update_notification(self, cron_mode=True):
        if version_info[5] == "e":
            return super().update_notification(cron_mode=cron_mode)
        return True
