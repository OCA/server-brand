# Copyright 2025 Milan Topuzov (https://milantopuzov.dev)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from lxml import html

from odoo import http
from odoo.tests import common


class _DummyRequest:
    class _Session:
        def __init__(self, debug=""):
            self.debug = debug

    def __init__(self, debug=""):
        # Minimal session object with a 'debug' attribute
        self.session = self._Session(debug=debug)

    def csrf_token(self, _):
        # Minimal CSRF call used by web.layout
        return ""


class TestWebOdooDebrandTitle(common.TransactionCase):
    def setUp(self):
        super().setUp()
        # Bind a dummy request into the http local stack so that the
        # `odoo.http.request` LocalProxy resolves during QWeb evaluation.
        self._dummy_request = _DummyRequest()
        http._request_stack.push(self._dummy_request)
        self.addCleanup(lambda: http._request_stack.pop())

    def test_web_layout_title_no_fallback(self):
        """web.layout should not fallback to 'Odoo' when no title is provided.

        Our view inherit replaces the <title> fallback with an empty string.
        Validate that the rendered document title is empty and contains no 'Odoo'.
        """
        content = self.env["ir.ui.view"]._render_template("web.layout", values={})
        doc = html.fromstring(content)
        titles = doc.xpath("//title")
        self.assertTrue(titles, "Rendered web.layout should contain a <title> tag")
        title_text = (titles[0].text or "").strip()
        self.assertEqual(title_text, "")
        self.assertNotIn("Odoo", title_text)

    def test_web_layout_title_with_value(self):
        """When a title value is provided, it should be rendered as-is."""
        expected = "My Custom Title"
        content = self.env["ir.ui.view"]._render_template(
            "web.layout", values={"title": expected}
        )
        doc = html.fromstring(content)
        titles = doc.xpath("//title")
        self.assertTrue(titles, "Rendered web.layout should contain a <title> tag")
        title_text = (titles[0].text or "").strip()
        self.assertEqual(title_text, expected)
