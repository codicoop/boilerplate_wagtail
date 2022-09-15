from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import InlinePanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.models import Collection, Orderable

from apps.base.models import BasePage, MenuLabelMixin


class CustomProjectsPage(MenuLabelMixin, BasePage):
    content_panels = BasePage.content_panels + [
        InlinePanel(
            "custom_projects",
            heading="Custom projects",
            label="Project",
        ),
    ]
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


class CustomProject(Orderable):
    page = ParentalKey(
        CustomProjectsPage,
        on_delete=models.CASCADE,
        related_name="custom_projects",
    )
    title = models.CharField(
        verbose_name=_("title"),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public"),
    )
    description = models.TextField(_("description"), default="", blank=True)
    images_collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
    )

    panels = [
        FieldPanel("title", classname="title"),
        FieldPanel("description", classname="full"),
    ]

    parent_page_types = ["cms_site.CustomProjectsPage"]
    page_description = _("Custom project page.")
    template = "pages/custom_projects/custom_project.html"
    show_in_menus_default = False
