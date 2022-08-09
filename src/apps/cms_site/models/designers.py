from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import StreamFieldPanel
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
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("designers_list"),
    ]

    template = "cms_site/collections/designers.html"
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(
            {
                "collections": Collection.objects.live(),
            }
        )
        return context
