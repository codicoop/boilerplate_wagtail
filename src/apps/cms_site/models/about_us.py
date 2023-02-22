from django.db import models
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
    video_description_1 = models.TextField(
        _("Video 1 description"),
        default="",
        blank=True,
    )
    video_description_2 = models.TextField(
        _("Video 2 description"),
        default="",
        blank=True,
    )
    video_description_3 = models.TextField(
        _("Video 3 description"),
        default="",
        blank=True,
    )
    video_description_4 = models.TextField(
        _("Video 4 description"),
        default="",
        blank=True,
    )
    video_description_5 = models.TextField(
        _("Video 5 description"),
        default="",
        blank=True,
    )
    video_description_6 = models.TextField(
        _("Video 6 description"),
        default="",
        blank=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("video_description_1"),
        FieldPanel("video_description_2"),
        FieldPanel("video_description_3"),
        FieldPanel("video_description_4"),
        FieldPanel("video_description_5"),
        FieldPanel("video_description_6"),
        FieldPanel("history_items_list"),
    ]

    template = "pages/about_us.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1
