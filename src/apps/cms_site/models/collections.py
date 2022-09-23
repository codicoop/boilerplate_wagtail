from django.apps import apps
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import InlinePanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.models import Orderable

from apps.base.models import BasePage, MenuLabelMixin


class CollectionsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    subpage_types = ["cms_site.Collection"]
    page_description = _("Main catalog page.")
    max_count = 1
    template = "pages/collections/page.html"

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

    content_panels = BasePage.content_panels + [
        FieldPanel("description"),
        FieldPanel("pdf"),
        InlinePanel(
            "collection_items",
            heading=_("Collection items"),
            label=_("Collection item"),
        ),
    ]

    template = "pages/collections/collection.html"
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
        """
        The Collection is going to have N items (the photo gallery), and we
        want the front to offer filters by Type, Finishing and Model.
        In order to limit the list of options in those filters to the ones that
        at least one of the CollectionItem contains, we loop through all of
        them.
        :return: { id: name }
        """
        available_types = {
            item_type.item_type.id: item_type.item_type.name
            for item in self.collection_items.all()
            for item_type in item.types.all()
        }
        return available_types

    def get_available_finishings(self):
        """
        See get_available_types comment.
        """
        available_finishings = {
            finishing.finishing.id: finishing.finishing.name
            for item in self.collection_items.all()
            for finishing in item.finishings.all()
        }
        return available_finishings

    def get_available_models(self):
        """
        See get_available_types comment
        """
        available_models = {
            item.model.id:item.model.name
            for item in self.collection_items.all()
        }
        return available_models


class CollectionItem(Orderable, ClusterableModel):
    page = ParentalKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="collection_items",
    )
    title = models.CharField(_("Title"), max_length=80)
    image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        related_name="+",
    )
    model = models.ForeignKey(
        "cms_site.CollectionItemModel",
        verbose_name=_("Model"),
        on_delete=models.CASCADE,
        help_text=mark_safe(
            _(
                "The model is not in the list? To add more, go to "
                "<a href=\"%(url)s\" target=\"_blank\">Snippets</a>."
            ) % {"url": "/cms/snippets/cms_site/collectionitemmodel/"}
        ),
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel("model"),
        InlinePanel(
            "finishings",
            heading=_("Finishings"),
            label=_("Finishing"),
        ),
        InlinePanel(
            "types",
            heading=_("Types"),
            label=_("Type"),
        ),
    ]

    def __str__(self):
        return self.title


class ItemFinishings(Orderable, models.Model):
    page = ParentalKey(CollectionItem, related_name="finishings")
    finishing = models.ForeignKey(
        "cms_site.CollectionItemFinishing",
        verbose_name=_("Finishing"),
        on_delete=models.CASCADE,
        help_text=mark_safe(
            _(
                "The finishing is not in the list? To add more, go to "
                "<a href=\"%(url)s\" target=\"_blank\">Snippets</a>."
            ) % {"url": "/cms/snippets/cms_site/collectionitemfinishing/"}
        ),
    )

    panels = [
        FieldPanel("finishing"),
    ]

    def __str__(self):
        return self.finishing.name


class ItemTypes(Orderable, models.Model):
    page = ParentalKey(CollectionItem, related_name="types")
    item_type = models.ForeignKey(
        "cms_site.CollectionItemType",
        verbose_name=_("Type"),
        on_delete=models.CASCADE,
        help_text=mark_safe(
            _(
                "The type is not in the list? To add more, go to "
                "<a href=\"%(url)s\" target=\"_blank\">Snippets</a>."
            ) % {"url": "/cms/snippets/cms_site/collectionitemtype/"}
        ),
    )

    panels = [
        FieldPanel("item_type"),
    ]

    def __str__(self):
        return self.item_type.name
