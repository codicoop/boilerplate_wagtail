from wagtail.core import blocks
from wagtail.core.blocks import ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from django.utils.translation import gettext_lazy as _


class CollectionItem(blocks.StructBlock):
    title = blocks.CharBlock(label=_("Title"))
    image = ImageChooserBlock(label=_("Image"))
    item_types = ListBlock(
        SnippetChooserBlock(
            target_model="cms_site.CollectionItemType",
            required=True,
            label=_("Type of furniture"),
        )
    )
    finishings = ListBlock(
        SnippetChooserBlock(
            target_model="cms_site.CollectionItemFinishing",
            required=True,
            label=_("Finishing"),
        )
    )

    class Meta:
        template = "cms_site/collections/block_item.html"
        icon = "doc-full"
