from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel

from apps.cms_site.blocks import CollectionItem


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
    items_list = CollectionItem()
    # next: programar Streampanel amb ListBlock, o Inline Panel, per la gestió
    # de les imatges.

    content_panels = Page.content_panels + [
        FieldPanel("name", classname="title"),
        FieldPanel("description"),
        DocumentChooserPanel("pdf"),
        # StreamFieldPanel("items_list"),
        # StreamBlock(),
    ]

    template = "cms_site/collection.html"
