from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.base.models import BasePage
from apps.cms_site.blocks import DesignerItem
from apps.cms_site.models import Collection


class DesignersPage(BasePage):
    designers_list = StreamField(
        [
            ("item", DesignerItem()),
        ],
        verbose_name=_("Compositions, renders and photos"),
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("designers_list"),
    ]

    template = "cms_site/collections/designers.html"
    max_count = 1
    parent_page_types = ["cms_site.HomePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            {
                "collections": Collection.objects.live(),
            }
        )
        return context
