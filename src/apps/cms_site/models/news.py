from apps.base.models import BasePage


class NewsPage(BasePage):
    template = "pages/news.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1
