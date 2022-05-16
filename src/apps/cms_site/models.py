from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    overlay_title = models.CharField(
        _("Title"),
        max_length=80,
        default="",
        blank=True,
    )
    overlay_body = models.TextField(_("Text"), default="", blank=True)
    overlay_button_text = models.CharField(
        _("Button title"),
        max_length=20,
        default="",
        blank=True,
    )
    overlay_button_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Linked page"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="+",
    )
    overlay_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_1_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    collection_1_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_1_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Collection's page"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="+",
    )
    collection_2_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    collection_2_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_2_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Collection's page"),
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            children=[
                FieldPanel("overlay_title", classname="title"),
                FieldPanel("overlay_body", classname="ful"),
                FieldPanel(
                    "overlay_button_text",
                ),
                PageChooserPanel(
                    "overlay_button_page",
                ),
                ImageChooserPanel(
                    "overlay_image",
                ),
            ],
            heading=_("Introduction overlaying header"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("collection_1_title", classname="title"),
                ImageChooserPanel("collection_1_image"),
                PageChooserPanel("collection_1_page"),
            ],
            heading=_("Image linking to the 1st collection"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("collection_2_title", classname="title"),
                ImageChooserPanel("collection_2_image"),
                PageChooserPanel("collection_2_page"),
            ],
            heading=_("Image linking to the 2nd collection"),
        ),
        # StreamFieldPanel("other_page_summaries"),
        # FieldPanel("publication_date"),
        # ImageChooserPanel("image"),
        # SnippetChooserPanel("category"),
    ]

    template = "cms_site/home.html"


class Collection(Page):
    name = models.CharField(_("name"), max_length=40)
    description = models.TextField(_("Description"), default="", blank=True)
    pdf = models.ForeignKey(
        'wagtaildocs.Document',
        verbose_name=_("Catalogue's PDF"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("name", classname="title"),
        FieldPanel("description"),
        DocumentChooserPanel("pdf"),
    ]

    template = "cms_site/collection.html"
