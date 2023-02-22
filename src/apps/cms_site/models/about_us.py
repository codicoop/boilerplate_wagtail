from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from django.utils.translation import gettext_lazy as _
from wagtail.models import Orderable

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
        InlinePanel(
            "video_items",
            heading=_("Videos"),
            label=_("Video"),
        ),
        InlinePanel(
            "history_items",
            heading=_("History"),
            label=_("History item"),
        ),
    ]

    template = "pages/about_us.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1


class VideoItem(Orderable, ClusterableModel):
    page = ParentalKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="video_items",
    )
    title = models.CharField(_("Title"), max_length=80)
    embed = models.TextField(_("Embed code"))
    description = models.TextField(_("Description"))

    panels = [
        FieldPanel("title"),
        FieldPanel("embed"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.title


class HistoryItem(Orderable, ClusterableModel):
    page = ParentalKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="history_items",
    )
    year = models.IntegerField(_("Year"))
    title = models.CharField(_("Title"), max_length=80)
    description = models.TextField(_("Description"))
    image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [
        FieldPanel("year"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title
