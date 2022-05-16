from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock


# class CollectionItemTypeChooserBlock(blocks.ChooserBlock):
#     widget = forms.Select
#     target_model = apps.get_model("cms_site", "CollectionItemType")
#
#     class Meta:
#         icon = "icon"
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def value_for_form(self, value):
#         if isinstance(value, self.target_model):
#             return value.pk
#         else:
#             return value
#
#


class CollectionItem(blocks.StructBlock):
    title = blocks.CharBlock()
    image = ImageChooserBlock()
    item_type = SnippetChooserBlock(
        target_model="cms_site.CollectionItemType",
        required=True
    )

    class Meta:
        icon = "doc-full"
