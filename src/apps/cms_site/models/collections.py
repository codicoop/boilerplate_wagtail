from django.apps import apps
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import HelpPanel, InlinePanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.models import Orderable
from wagtailautocomplete.edit_handlers import AutocompletePanel

from apps.base.models import BasePage, MenuLabelMixin


class CollectionsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    subpage_types = ["cms_site.Collection"]
    page_description = _("Main catalog page.")
    max_count = 1
    template = "pages/collections/page.html"

    content_panels = BasePage.content_panels + [
        HelpPanel(
            _(
                "To manage the list of collections that appear in this section"
                " you must edit the Home page, as the information is taken "
                "from there."
            )
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        """
        Passing the home page to the view because for the list of collections
        we'll be using the configuration set there.
        """
        home_page_model = apps.get_model("cms_site", "HomePage")
        home_page_obj = home_page_model.objects.first()
        context.update(
            {
                "home_page": home_page_obj or None,
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
                "collections": self.get_siblings(True),
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
            item_type.id: item_type.title
            for item in self.collection_items.all()
            for item_type in item.typologies.all()
        }
        return available_types

    def get_available_finishings(self):
        """
        See get_available_types comment.
        """
        available_finishings = {
            finishing.id: finishing.title
            for item in self.collection_items.all()
            for finishing in item.finishings.all()
        }
        return available_finishings

    def get_available_models(self):
        """
        See get_available_types comment
        """
        available_models = {
            item.model.id: item.model.name for item in self.collection_items.all()
        }
        return available_models

    def __str__(self):
        return self.title


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
                '<a href="%(url)s" target="_blank">Models</a>.'
            )
            % {"url": "/cms/snippets/cms_site/collectionitemmodel/"}
        ),
    )
    finishings = ParentalManyToManyField(
        "cms_site.CollectionItemFinishing",
        related_name="finishings",
        help_text=mark_safe(
            _(
                "The finishing is not in the list? To add more, go to "
                '<a href="%(url)s" target="_blank">Finishings</a>.'
            )
            % {"url": "/cms/snippets/cms_site/collectionitemfinishing/"}
        ),
    )
    typologies = ParentalManyToManyField(
        "cms_site.CollectionItemType",
        related_name="typologies",
        help_text=mark_safe(
            _(
                "The type is not in the list? To add more, go to "
                '<a href="%(url)s" target="_blank">Typologies</a>.'
            )
            % {"url": "/cms/snippets/cms_site/collectionitemtype/"}
        ),
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel("model"),
        AutocompletePanel(
            "typologies",
            target_model="cms_site.CollectionItemType",
        ),
        AutocompletePanel(
            "finishings",
            target_model="cms_site.CollectionItemFinishing",
        ),
    ]

    def __str__(self):
        return self.title
