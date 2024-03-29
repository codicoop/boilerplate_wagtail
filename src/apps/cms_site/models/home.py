from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page

from apps.base.models import BasePage


class HomePage(BasePage):
    overlay_title = models.CharField(
        _("Title"),
        max_length=80,
        default="",
        blank=True,
    )
    overlay_body = models.TextField(_("Text"), default="", blank=True)
    overlay_button_text = models.CharField(
        _("Button title"),
        max_length=20,
        default="",
        blank=True,
    )
    overlay_button_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Linked page"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overlay_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_1_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    collection_1_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_1_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Collection's page"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    collection_2_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    collection_2_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_2_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Collection's page"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    collection_3_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    collection_3_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    collection_3_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Collection's page"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    custom_projects_title = models.CharField(
        _("Title"),
        max_length=40,
        default="",
        blank=True,
    )
    custom_projects_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    custom_projects_page = models.ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("Custom projects' page"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    display_instagram_feed = models.BooleanField(
        _("Display Instagram feed section"),
        default=True,
    )
    display_header_highlight = models.BooleanField(
        _("Display header highlighted overlay"),
        default=True,
    )

    content_panels = BasePage.content_panels + [
        MultiFieldPanel(
            children=[
                FieldPanel("overlay_title", classname="title"),
                FieldPanel("overlay_body", classname="full"),
                FieldPanel(
                    "overlay_button_text",
                ),
                FieldPanel(
                    "overlay_button_page",
                ),
                FieldPanel(
                    "overlay_image",
                ),
            ],
            heading=_("Introduction overlaying header"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("collection_1_title", classname="title"),
                FieldPanel("collection_1_image"),
                FieldPanel("collection_1_page"),
            ],
            heading=_("Image linking to the 1st collection"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("collection_2_title", classname="title"),
                FieldPanel("collection_2_image"),
                FieldPanel("collection_2_page"),
            ],
            heading=_("Image linking to the 2nd collection"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("collection_3_title", classname="title"),
                FieldPanel("collection_3_image"),
                FieldPanel("collection_3_page"),
            ],
            heading=_("Image linking to the 3rd collection"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("custom_projects_title", classname="title"),
                FieldPanel("custom_projects_image"),
                FieldPanel("custom_projects_page"),
            ],
            heading=_("Custom projects block"),
        ),
    ]
    settings_panels = [
        MultiFieldPanel(
            [
                FieldPanel("display_instagram_feed"),
                FieldPanel("display_header_highlight"),
            ],
            heading=_("Section's visibility configuration"),
        ),
    ] + Page.settings_panels

    template = "pages/home.html"
    parent_page_types = ["wagtailcore.Page"]

    @property
    def display_collection_1(self):
        return (
            self.collection_1_page
            and self.collection_1_image
            and self.collection_1_title
        )

    @property
    def display_collection_2(self):
        return (
            self.collection_2_page
            and self.collection_2_image
            and self.collection_2_title
        )

    @property
    def display_collection_3(self):
        return (
            self.collection_3_page
            and self.collection_3_image
            and self.collection_3_title
        )

    @property
    def display_collections_section(self):
        return (
            self.display_collection_1
            or self.display_collection_2
            or self.display_collection_3
        )

    @property
    def display_custom_projects_section(self):
        return (
            self.custom_projects_page
            and self.custom_projects_image
            and self.custom_projects_title
        )

    def can_display_header_highlight(self):
        return (
            self.display_header_highlight
            and self.overlay_image
            and self.overlay_body
            and self.overlay_title
        )

    def get_context(self, request, *args, **kwargs):
        ctxt = super().get_context(request, *args, **kwargs)
        ctxt = self.add_news_to_context(ctxt)
        ctxt = self.add_posts_to_context(ctxt)
        return ctxt

    def add_news_to_context(self, context):
        news_model = apps.get_model("cms_site", "NewsPage")
        news_page = news_model.objects.first()
        if news_page:
            context.update(
                {
                    "news_url": news_page.localized.get_url(),
                }
            )
            return context
        return context

    def add_posts_to_context(self, context):
        instagram_post_model = apps.get_model("cms_site", "InstagramPost")
        posts = instagram_post_model.objects.all()[:3]
        if posts:
            context.update(
                {
                    "instagram_posts": posts,
                },
            )
            return context
        return context
