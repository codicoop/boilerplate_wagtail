from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

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
    description = models.TextField(_("Description"), default="", blank=True)
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
    images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel("main_section_image"),
        MultiFieldPanel(
            [
                FieldPanel("images"),
            ],
            heading=_("Image gallery"),
        ),
    ]

    parent_page_types = ["cms_site.CustomProjectsPage"]
    page_description = _("Custom project page.")
    template = "pages/custom_projects/custom_project.html"
    show_in_menus_default = False
