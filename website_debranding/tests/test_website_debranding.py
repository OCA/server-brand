from odoo.addons.base.tests.common import BaseCommon


class TestWebsiteDebranding(BaseCommon):
    _test_user_groups = None

    def test_brand_promotion_removed(self):
        self.env.ref("website_debranding.layout_footer_copyright").active = True
        html = str(self.env["ir.qweb"]._render("web.brand_promotion", {}))
        self.assertNotIn("Powered by", html)
