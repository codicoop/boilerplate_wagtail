from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class PageSummary(blocks.StructBlock):
    title = blocks.CharBlock()
    linked_page = blocks.PageChooserBlock(
        # page_type="appname.PageModelName",
    )
    image = ImageChooserBlock()

    class Meta:
        icon = "doc-full"
