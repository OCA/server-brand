# Copyright 2016 LasLabs Inc.
# Copyright 2018-2020 Onestein (<http://www.onestein.eu>)
# Copyright 2023 Le Filament (https://le-filament.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def get_views(self, views, options=None):
        ret_val = super().get_views(views, options)

        form_view = self.env["ir.ui.view"].browse(ret_val["views"]["form"]["id"])
        if not form_view.xml_id == "base.res_config_settings_view_form":
            return ret_val

        doc = etree.XML(ret_val["views"]["form"]["arch"])

        query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(query):
            item.attrib["class"] = "d-none"

        ret_val["views"]["form"]["arch"] = etree.tostring(doc)
        return ret_val
