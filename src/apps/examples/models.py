from wagtail.models import Page


class ExamplesPage(Page):
    # overlay_title = models.CharField(
    #     _("Title"),
    #     max_length=80,
    #     default="",
    #     blank=True,
    # )
    # overlay_body = models.TextField(_("Text"), default="", blank=True)
    # overlay_button_text = models.CharField(
    #     _("Button title"),
    #     max_length=20,
    #     default="",
    #     blank=True,
    # )
    # overlay_button_page = models.ForeignKey(
    #     "wagtailcore.Page",
    #     verbose_name=_("Linked page"),
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT,
    #     related_name="+",
    # )
    # overlay_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     verbose_name=_("Image"),
    #     on_delete=models.PROTECT,
    #     related_name="+",
    #     null=True,
    #     blank=True,
    # )
    # collection_1_title = models.CharField(
    #     _("Title"),
    #     max_length=40,
    #     default="",
    #     blank=True,
    # )
    # collection_1_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     verbose_name=_("Image"),
    #     on_delete=models.PROTECT,
    #     related_name="+",
    #     null=True,
    #     blank=True,
    # )
    # collection_1_page = models.ForeignKey(
    #     "wagtailcore.Page",
    #     verbose_name=_("Collection's page"),
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT,
    #     related_name="+",
    # )
    # collection_2_title = models.CharField(
    #     _("Title"),
    #     max_length=40,
    #     default="",
    #     blank=True,
    # )
    # collection_2_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     verbose_name=_("Image"),
    #     on_delete=models.PROTECT,
    #     related_name="+",
    #     null=True,
    #     blank=True,
    # )
    # collection_2_page = models.ForeignKey(
    #     "wagtailcore.Page",
    #     verbose_name=_("Collection's page"),
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT,
    #     related_name="+",
    # )
    #
    # content_panels = Page.content_panels + [
    #     MultiFieldPanel(
    #         children=[
    #             FieldPanel("overlay_title", classname="title"),
    #             FieldPanel("overlay_body", classname="full"),
    #             FieldPanel(
    #                 "overlay_button_text",
    #             ),
    #             PageChooserPanel(
    #                 "overlay_button_page",
    #             ),
    #             FieldPanel(
    #                 "overlay_image",
    #             ),
    #         ],
    #         heading=_("Introduction overlaying header"),
    #     ),
    #     MultiFieldPanel(
    #         [
    #             FieldPanel("collection_1_title", classname="title"),
    #             FieldPanel("collection_1_image"),
    #             PageChooserPanel("collection_1_page"),
    #         ],
    #         heading=_("Image linking to the 1st collection"),
    #     ),
    #     MultiFieldPanel(
    #         [
    #             FieldPanel("collection_2_title", classname="title"),
    #             FieldPanel("collection_2_image"),
    #             PageChooserPanel("collection_2_page"),
    #         ],
    #         heading=_("Image linking to the 2nd collection"),
    #     ),
    #     # FieldPanel("other_page_summaries"),
    #     # FieldPanel("publication_date"),
    #     # FieldPanel("image"),
    #     # FieldPanel("category"),
    # ]
    pass
