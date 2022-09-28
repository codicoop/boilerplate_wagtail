from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class DesignerItem(blocks.StructBlock):
    quote = blocks.CharBlock(label=_("Quote"))
    name = blocks.CharBlock(label=_("Name"))
    role = blocks.CharBlock(
        label=_("Role"),
        help_text=_("I.e.: 'Area collection designer'"),
    )
    description = blocks.CharBlock(label=_("Description"))
    photo = ImageChooserBlock(label=_("Photo"))

    class Meta:
        template = "cms_site/collections/block_designer.html"
        icon = "doc-full"
