from django.apps import apps
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import HelpPanel, InlinePanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.models import Orderable, Page, TranslatableMixin
from wagtailautocomplete.edit_handlers import AutocompletePanel

from apps.base.models import BasePage, MenuLabelMixin


class CollectionsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    subpage_types = ["cms_site.Collection"]
    page_description = _("Main catalog page.")
    template = "pages/collections/page.html"
    header_image = None

    # Grabbing panels from Page instead of BasePage because in this one we are
    # not including header_image.
    content_panels = Page.content_panels + [
        HelpPanel(
            _(
                "In the Collections section, we show the user the different "
                "collections in a full-screen sized mosaic of pictures."
                "These pictures are the same than the collections shown in the "
                "Home page."
                "Therefore, if you want to change the content of this section, you "
                "must edit the fields 'Image linking to the 1st collection', "
                "'Image linking to the 2nd collection' and 'Image linking to "
                "the 3rd collection' that you will find when editing the Home "
                "page."
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
        home_page_obj = home_page_model.objects.requested_locale(request).first()
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
    is_unpublishable = True

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        designers_page_model = apps.get_model("cms_site", "DesignersPage")
        designers_page = designers_page_model.objects.live().first()
        collections = self.get_submenu()

        context.update(
            {
                "available_types": self.get_available_types(),
                "available_finishings": self.get_available_finishings(),
                "available_models": self.get_available_models(),
                "collections": collections,
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
            item_type.id: item_type.localized
            for item in self.get_instance_for_lang_code().collection_items.all()
            for item_type in item.typologies.all()
        }
        return available_types

    def get_available_finishings(self):
        """
        See get_available_types comment.
        """
        available_finishings = {
            finishing.id: finishing.localized
            for item in self.get_instance_for_lang_code().collection_items.all()
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

    def get_submenu(self):
        return [
            {
                "active_class": "is-active" if collection.specific == self else "",
                "page": collection,
            }
            for collection in self.get_siblings(True)
        ]

    def __str__(self):
        return self.title

    def get_instance_for_lang_code(self, code="ca"):
        return Collection.objects.get(
            locale=self.get_locale_for_lang_code(code),
            translation_key=self.translation_key,
        )


class CollectionItem(TranslatableMixin, Orderable, ClusterableModel):
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
        help_text=_(
            "To avoid cutting the picture in the thumbnail, the "
            "uploaded image should have a 1x1 proportion. Minimum recommended "
            "size is 2.000x2.000px."
        ),
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
            % {"url": "/cms/cms_site/collectionitemmodel/"}
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
            % {"url": "/cms/cms_site/collectionitemfinishing/"}
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
            % {"url": "/cms/cms_site/collectionitemtype/"}
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
