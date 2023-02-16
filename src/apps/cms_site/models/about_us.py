from apps.base.models import BasePage


class AboutUsPage(BasePage):
    template = "pages/about_us.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1
