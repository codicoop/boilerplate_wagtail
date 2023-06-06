from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from apps.base.models import BasePage, MenuLabelMixin
from apps.wagtail_ajax_contact_form.models import AjaxContactPage, ContactSubmission


class CustomAjaxContact(MenuLabelMixin, AjaxContactPage):
    class Meta:
        verbose_name = _("Contact page")

    # Camps
    subject_label = models.CharField(
        _("subject"),
        max_length=250,
        help_text=_("Label for the Subject field."),
        default=_("Subject"),
    )
    phone_label = models.CharField(
        _("phone"),
        max_length=250,
        help_text=_("Label for the Phone field."),
        default=_("Phone"),
    )
    profile_label = models.CharField(
        _("profile"),
        max_length=250,
        help_text=_("Label for the Profile field."),
        default=_("Profile"),
    )
    personal_data_auth_label = models.CharField(
        _("personal data treatment"),
        max_length=250,
        help_text=_("Label for the Personal data treatment checkbox."),
        default=_("Treatment of personal data authorization"),
    )
    personal_data_comercial_auth_label = models.CharField(
        _("personal data for comercial use treatment"),
        max_length=250,
        help_text=_(
            "Label for the Personal data for comercial use treatment checkbox."
        ),
        default=_("Treatment of personal data authorization for comercial purposes"),
    )

    """
    Instead of extending AjaxContactPage' panels, we override it the same way
    we did in the other pages, by extending the BasePage one, but using the
    available lists like AjaxContactPage.field_labels to reuse the code.
    """
    content_panels = BasePage.content_panels + [
        MultiFieldPanel(
            AjaxContactPage.field_labels
            + [
                FieldPanel("subject_label", classname="full"),
                FieldPanel("phone_label", classname="full"),
                FieldPanel("profile_label", classname="full"),
                FieldPanel("personal_data_auth_label", classname="full"),
                FieldPanel(
                    "personal_data_comercial_auth_label",
                    classname="full",
                ),
            ],
            heading=_("Field labels"),
        ),
        MultiFieldPanel(
            AjaxContactPage.form_settings,
            heading=_("Form settings"),
        ),
    ]

    template = "pages/contact_ajax.html"

    @classmethod
    def get_contact_form(cls):
        from apps.cms_site.forms import ContactFormAjax

        return ContactFormAjax


class AjaxContactSubmission(ContactSubmission):
    subject = models.CharField(
        _("subject"),
        max_length=120,
        default="",
        blank=True,
    )
    phone = models.CharField(
        _("phone"),
        max_length=120,
        default="",
        blank=True,
    )
    profile = models.CharField(
        _("profile"),
        max_length=120,
        default="",
        blank=True,
    )
    personal_data_auth = models.BooleanField(
        _("Treatment of personal data authorization"),
    )
    personal_data_comercial_auth = models.BooleanField(
        _("Treatment of personal data authorization for comercial purposes"),
    )
