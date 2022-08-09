from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.blocks import ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


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
        ),
        required=False,
    )
    model = SnippetChooserBlock(
        target_model="cms_site.CollectionItemModel",
        required=True,
        label=_("Model"),
    )

    class Meta:
        template = "cms_site/collections/block_item.html"
        icon = "doc-full"


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
