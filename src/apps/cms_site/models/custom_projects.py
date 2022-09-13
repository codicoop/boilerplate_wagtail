from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.documents.edit_handlers import FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from apps.base.models import BasePage, MenuLabelMixin


class CustomProjectsPage(MenuLabelMixin, BasePage):
    parent_page_types = ["cms_site.HomePage"]
    page_description = _("Main page for custom projects section.")
    max_count = 1
    template = "pages/custom_projects_page.html"
    show_in_menus_default = True


class CustomProject(BasePage):
    description = models.TextField(_("Description"), default="", blank=True)
    images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
    )
s pàgine
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("images"),
    ]

    parent_page_types = ["cms_site.CustomProjectsPage"]
    page_description = _("Custom project page.")
    template = "pages/custom_project.html"
    show_in_menus_default = False
