from django.db import models
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from django.utils.translation import gettext_lazy as _


@register_setting
class SocialMediaIconsSettings(BaseSetting):
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
        default="https://www.instagram.com/moblesciurans",
    )
    vimeo = models.URLField(
        blank=True,
        null=True,
        help_text=_("Vimeo URL"),
        default="https://vimeo.com/moblesciurans",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("youtube"),
            FieldPanel("instagram"),
            FieldPanel("vimeo"),
        ], heading=_("Social Media URLs"))
    ]


@register_setting
class ContactDetailsSettings(BaseSetting):
    email = models.EmailField(
        blank=True,
        null=True,
        help_text=_("Direct e-mail"),
        default="info@moblesciurans.com",
    )
    address = models.URLField(
        blank=True,
        null=True,
        help_text=_("Telegram URL"),
        default="""C/ Priora Xixilona, 14
        08530 La Garriga
        Barcelona""",
    )
    phone = models.URLField(
        blank=True,
        null=True,
        help_text=_("Whatsapp URL"),
        default="93 871 80 07",
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("email"),
            FieldPanel("address"),
            FieldPanel("phone"),
        ], heading=_("Contact Details"))
    ]
