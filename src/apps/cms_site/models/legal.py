from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from apps.base.models import BasePage


class LegalPage(BasePage):
    text = RichTextField(
        _("Text"),
        features=[
            "h2",
            "h3",
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
        ],
    )
    content_panels = BasePage.content_panels + [
        FieldPanel(
            "text",
        ),
    ]

    template = "pages/legal.html"
    parent_page_types = ["cms_site.HomePage"]
