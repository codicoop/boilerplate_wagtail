from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page, TranslatableMixin
from wagtail.snippets.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"


class StoryBlock(blocks.StreamBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image = ImageBlock()


@register_snippet
class BlogCategory(TranslatableMixin):
    name = models.CharField(max_length=255)

    class Meta(TranslatableMixin.Meta):
        verbose_name = _("Blog category")
        verbose_name_plural = _("Blog categories")

    def __str__(self):
        return self.name


class BlogPostPage(Page):
    publication_date = models.DateField(null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True
    )
    body = StreamField(StoryBlock(), use_json_field=True)
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, related_name="blog_posts"
    )

    content_panels = Page.content_panels + [
        FieldPanel("publication_date"),
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel("category"),
    ]

    parent_page_types = ["blog.BlogIndexPage"]
    template = "blog/post.html"


class BlogIndexPage(Page):
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = ["cms_site.HomePage"]
    subpage_types = ["blog.BlogPostPage"]
    template = "blog/index.html"
