from apps.base.models import BasePage


class ContactPage(BasePage):
    template = "pages/contact.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1
