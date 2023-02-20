from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from django.utils.translation import gettext_lazy as _

from apps.base.models import BasePage, MenuLabelMixin
from apps.wagtail_ajax_contact_form.models import AjaxContactPage


class ContactPage(BasePage):
    template = "pages/contact.html"
    parent_page_types = ["cms_site.HomePage"]
    max_count = 1


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

    """
    Instead of extending AjaxContactPage' panels, we override it the same way
    we did in the other pages, by extending the BasePage one, but using the
    available lists like AjaxContactPage.field_labels to reuse the code.
    """
    content_panels = BasePage.content_panels + [
        MultiFieldPanel(
            AjaxContactPage.field_labels +
            [
                FieldPanel('subject_label', classname="full"),
                FieldPanel('phone_label', classname="full"),
                FieldPanel('profile_label', classname="full"),
            ],
            heading=_("Field labels"),
        ),
        MultiFieldPanel(
            AjaxContactPage.form_settings,
            heading=_("Form settings"),
        ),
    ]

    max_count = 1
    template = 'cms/contact_us.html'
