from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from django.utils.translation import gettext_lazy as _

from apps.base.models import BasePage
from apps.cms_site.blocks import AboutUsHistoryItem


class AboutUsPage(BasePage):
    history_items_list = StreamField(
        [
            ("item", AboutUsHistoryItem()),
        ],
        verbose_name=_("History points"),
        use_json_field=True,
        null=True,
        blank=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("history_items_list"),
    ]

    template = "pages/about_us.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1
