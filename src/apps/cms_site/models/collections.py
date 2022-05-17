from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
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
    items_list = StreamField(
        [
            ("item", CollectionItem()),
        ],
        verbose_name=_("Compositions, renders and photos"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("name", classname="title"),
        FieldPanel("description"),
        DocumentChooserPanel("pdf"),
        StreamFieldPanel("items_list"),
    ]

    template = "cms_site/collections/collection.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    # def get_available_types(self):
    #     r =
    #
