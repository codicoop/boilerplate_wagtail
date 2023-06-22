from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, TranslatableMixin

from apps.base.models import BasePage


class AboutUsForm(WagtailAdminPageForm):
    def clean(self):
        cleaned_data = super().clean()
        # We cannot do this validation in AboutUsPage.clean because the videos
        # are a kind of m2m data, and when it calls .clean() the m2m data of
        # the model is not saved yet so we could only access the "old" data
        # but not the one just send in the form.
        # This post explain the "formsets" solution used here:
        # https://github.com/wagtail/wagtail/issues/3175#issuecomment-513917840
        if len(self.formsets["video_items"].forms) != 6:
            raise ValidationError(
                # Having to use non field errors as there's not a field called
                # "video_items".
                {
                    NON_FIELD_ERRORS: _(
                        "There need to be exactly 6 videos to be able to save "
                        "the changes."
                    )
                }
            )
        return cleaned_data


class AboutUsPage(BasePage):
    description = RichTextField(
        _("Description"),
        default="",
        blank=True,
        features=[
            "h2",
            "h3",
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
        ],
    )
    content_panels = BasePage.content_panels + [
        FieldPanel("description"),
        InlinePanel(
            "video_items",
            heading=_("Videos"),
            label=_("Video"),
        ),
        InlinePanel(
            "history_items",
            heading=_("History"),
            label=_("History item"),
        ),
    ]

    template = "pages/about_us.html"
    parent_page_types = ["cms_site.HomePage"]
    base_form_class = AboutUsForm


class VideoItem(TranslatableMixin, Orderable, ClusterableModel):
    page = ParentalKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="video_items",
    )
    title = models.CharField(_("Title"), max_length=80)
    embed = models.TextField(_("Embed code"))
    description = models.TextField(_("Description"))

    panels = [
        FieldPanel("title"),
        FieldPanel("embed"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.title


class HistoryItem(TranslatableMixin, Orderable, ClusterableModel):
    page = ParentalKey(
        AboutUsPage,
        on_delete=models.CASCADE,
        related_name="history_items",
    )
    year = models.IntegerField(_("Year"))
    title = models.CharField(_("Title"), max_length=80)
    description = models.TextField(_("Description"))
    image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [
        FieldPanel("year"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title
