from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


class CollectionItem(blocks.StructBlock):
    title = blocks.CharBlock()
    image = ImageChooserBlock()
    item_type = SnippetChooserBlock(
        target_model="cms_site.CollectionItemType",
        required=True
    )

    class Meta:
        icon = "doc-full"
