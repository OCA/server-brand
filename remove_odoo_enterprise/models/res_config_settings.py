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
        """Override to hide settings related to enterprise features.

        This method modifies the form view for settings to hide options
        that require enterprise version of Odoo.
        """
        result = super().get_views(views, options)

        doc = etree.XML(result["views"]["form"]["arch"])

        # Hide all setting boxes containing upgrade_boolean widgets
        self._hide_enterprise_settings(doc)

        # Hide empty setting containers and their headings
        self._hide_empty_containers(doc)

        # Update the form view architecture with the modified XML
        result["views"]["form"]["arch"] = etree.tostring(doc)
        return result

    def _hide_enterprise_settings(self, doc):
        """Hide all setting boxes containing upgrade_boolean widgets."""
        # Find all setting boxes with upgrade_boolean widgets
        query = (
            "//div[contains(@class, 'o_setting_box')]"
            "[.//field[@widget='upgrade_boolean']]"
        )
        for setting_box in doc.xpath(query):
            setting_box.attrib["class"] = "d-none"

    def _hide_empty_containers(self, doc):
        """Hide containers that no longer have any visible setting boxes."""
        # Find containers with no visible setting boxes
        empty_container_query = (
            "//div[contains(@class, 'o_settings_container')]"
            "[not(.//div[contains(@class, 'o_setting_box') "
            "and not(contains(@class, 'd-none'))])]"
        )

        for empty_container in doc.xpath(empty_container_query):
            # If there's a heading before the container, hide it too
            prev_element = empty_container.getprevious()
            if prev_element is not None and prev_element.tag == "h2":
                prev_element.attrib["class"] = "d-none"
            # Hide the empty container
            empty_container.attrib["class"] = "d-none"
