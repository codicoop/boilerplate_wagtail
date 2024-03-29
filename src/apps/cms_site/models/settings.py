from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting
class SocialMediaIconsSettings(BaseSiteSetting):
    facebook = models.URLField(
        blank=True,
        null=True,
        help_text=_("Facebook URL"),
        default="https://www.facebook.com/moblesciurans",
    )
    youtube = models.URLField(
        blank=True,
        null=True,
        help_text=_("Youtube URL"),
        default="http://www.youtube.com/user/ciuransmobles",
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        help_text=_("Instagram URL"),
        default="https://www.instagram.com/ciuransmobles",
    )
    vimeo = models.URLField(
        blank=True,
        null=True,
        help_text=_("Vimeo URL"),
        default="https://vimeo.com/moblesciurans",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("youtube"),
                FieldPanel("instagram"),
                FieldPanel("vimeo"),
            ],
            heading=_("Social Media URLs"),
        )
    ]


@register_setting
class ContactDetailsSettings(BaseSiteSetting):
    email = models.EmailField(
        blank=True,
        null=True,
        help_text=_("Contact e-mail"),
        default="info@moblesciurans.com",
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text=_("Address"),
        default="""C/ Priora Xixilona, 14<br>
        08530 La Garriga<br>
        Barcelona""",
    )
    phone = models.CharField(
        blank=True,
        null=True,
        help_text=_("Phone number"),
        default="93 871 80 07",
        max_length=30,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("address"),
                FieldPanel("phone"),
            ],
            heading=_("Contact Details"),
        )
    ]


@register_setting
class AnalyticsSettings(BaseSiteSetting):
    embed = models.TextField(
        _("Embed code"),
        default="",
        blank=True,
    )

    panels = [
        FieldPanel("embed"),
    ]
