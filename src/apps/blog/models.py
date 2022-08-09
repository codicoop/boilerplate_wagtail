from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import Page, TranslatableMixin
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
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
    body = StreamField(StoryBlock())
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, related_name="blog_posts"
    )

    content_panels = Page.content_panels + [
        FieldPanel("publication_date"),
        ImageChooserPanel("image"),
        StreamFieldPanel("body"),
        SnippetChooserPanel("category"),
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
