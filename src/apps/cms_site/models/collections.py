from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel

from apps.base.models import BasePage
from apps.cms_site.blocks import CollectionItem


class Collection(BasePage):
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
        context.update({
            "available_types": self.get_available_types(),
            "available_finishings": self.get_available_finishings(),
            "available_models": self.get_available_models(),
            "collections": self.get_siblings(False),
        })
        return context

    def get_available_types(self):
        available_types = set()
        for item in self.items_list:
            available_types = {
                item_type
                for item_type in dict(item.__dict__["value"])["item_types"]
            }
        return available_types

    def get_available_finishings(self):
        available_finishings = set()
        for item in self.items_list:
            available_finishings = {
                finishing
                for finishing in dict(item.__dict__["value"])["finishings"]
            }
        return available_finishings

    def get_available_models(self):
        available_models = set()
        for item in self.items_list:
            available_models.add(dict(item.__dict__["value"])["model"])
        return available_models
