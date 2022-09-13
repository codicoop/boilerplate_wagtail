from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.fields import StreamField

from apps.base.models import BasePage, MenuLabelMixin
from apps.cms_site.blocks import CollectionItem


class CollectionsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    subpage_types = ["cms_site.Collection"]
    page_description = _("Main catalog page.")
    max_count = 1
    template = "pages/collections_page.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        collection_page_model = apps.get_model("cms_site", "Collection")
        collection_pages = collection_page_model.objects.live()
        context.update(
            {
                "collections": collection_pages,
            }
        )
        return context


class Collection(BasePage):
    description = models.TextField(_("Description"), default="", blank=True)
    pdf = models.ForeignKey(
        "wagtaildocs.Document",
        verbose_name=_("Catalogue's PDF"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    items_list = StreamField(
        [
            ("item", CollectionItem()),
        ],
        verbose_name=_("Compositions, renders and photos"),
        use_json_field=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("description"),
        FieldPanel("pdf"),
        FieldPanel("items_list"),
    ]

    template = "cms_site/collections/collection.html"
    parent_page_types = ["CollectionsPage"]
    max_count = 3

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        designers_page_model = apps.get_model("cms_site", "DesignersPage")
        designers_page = designers_page_model.objects.live().first()
        context.update(
            {
                "available_types": self.get_available_types(),
                "available_finishings": self.get_available_finishings(),
                "available_models": self.get_available_models(),
                "collections": self.get_siblings(False),
                "designers_page": designers_page,
            }
        )
        return context

    def get_available_types(self):
        available_types = set()
        for item in self.items_list:
            available_types = {
                item_type for item_type in dict(item.__dict__["value"])["item_types"]
            }
        return available_types

    def get_available_finishings(self):
        available_finishings = set()
        for item in self.items_list:
            available_finishings = {
                finishing for finishing in dict(item.__dict__["value"])["finishings"]
            }
        return available_finishings

    def get_available_models(self):
        available_models = set()
        for item in self.items_list:
            available_models.add(dict(item.__dict__["value"])["model"])
        return available_models
