from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import HelpPanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.models import Collection, get_root_collection_id

from apps.base.models import BasePage, MenuLabelMixin


class CustomProjectsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    page_description = _("Main page for custom projects section.")
    max_count = 1
    template = "pages/custom_projects/page.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        collection_page_model = apps.get_model("cms_site", "CustomProject")
        collection_pages = collection_page_model.objects.live()
        context.update(
            {
                "custom_projects": collection_pages,
            }
        )
        return context


class CustomProject(BasePage):
    description = models.TextField(_("description"), default="", blank=True)
    main_section_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Main section image"),
        on_delete=models.PROTECT,
        related_name="+",
        null=False,
        blank=False,
        help_text="This image will be used in the Custom Projects section, "
                  "when displaying the list of projects."
    )
    images_collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel("main_section_image"),
        HelpPanel(_(
            "To manage the project's photos, firstly save this page's changes "
            "(either as Draft or Published) and then go to the "
            "<a href=\"/cms/images\">%(url_label)s</a>, "
            "select the collection with the same namne as this project and "
            "there add the images."
            # "Per gestionar les fotos del projecte, val que desis (com a "
            # "Esborrany o Publicat) els canvis que estiguis fent i després anar"
            # " al <a href=\"/cms/images\">%(url_label)</a>, seleccionar la "
            # "col·lecció amb el mateix nom que el projecte, i allà afegir "
            # "les imatges."
        ) % {"url_label": "Images section"}),
    ]

    parent_page_types = ["cms_site.CustomProjectsPage"]
    page_description = _("Custom project page.")
    template = "pages/custom_projects/custom_project.html"

    def save(self, clean=True, user=None, log_action=False, **kwargs):
        self.create_or_update_collection()
        return super().save(clean, user, log_action, **kwargs)

    def create_or_update_collection(self):
        """
        Each Custom Project needs to have a Collection linked through the
        CustomProject.images_collection field, but we don't want the editor
        to have to create the collection and then manually link it to the
        project somehow.

        When a Custom Project is created a collection will be created with
        the same name than the project's title.
        If modified, the collection's name will be updated.
        If deleted, the collection will be deleted as well (we don't have to
        handled that as the on_delete property is CASCADE)
        """
        collection_name = f"[Projecte a mida] {self.title}"
        if not self.images_collection:
            root_node = Collection.objects.get(id=get_root_collection_id())
            new_collection = root_node.add_child(name=collection_name)
            self.images_collection = new_collection
        else:
            self.images_collection.name = collection_name
            self.images_collection.save()

    def get_context(self, request, *args, **kwargs):
        ct = super().get_context(request, *args, **kwargs)
        ct["images"] = []
        if self.images_collection:
            ct["images"] = Image.objects.filter(
                collection=self.images_collection,
            )
        return ct
