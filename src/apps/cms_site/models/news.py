from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Orderable

from apps.base.models import BasePage


class NewsPage(BasePage):
    content_panels = BasePage.content_panels + [
        InlinePanel(
            "instagram_posts",
            heading=_("Instagram posts"),
            label=_("Instagram post"),
        ),
    ]

    template = "pages/news.html"
    parent_page_types = ["cms_site.HomePage"]


class InstagramPost(Orderable, ClusterableModel):
    page = ParentalKey(
        NewsPage,
        on_delete=models.CASCADE,
        related_name="instagram_posts",
    )
    url = models.CharField(
        _("Link to post"),
        max_length=80,
        help_text=_("Example: https://www.instagram.com/p/CfyTUDfIxeY"),
    )

    panels = [
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.url
