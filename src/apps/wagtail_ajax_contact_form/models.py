import json

from django.http import JsonResponse
from django.db import models
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField

from apps.base.models import BasePage


class AjaxContactPage(RoutablePageMixin, BasePage):
    # Leaving the option to create this page in admin disabled by default
    # assuming you will subclass it to your custom needs.
    is_creatable = False

    # Form fields
    name_label = models.CharField(
        _("name"),
        max_length=250,
        help_text=_("Label for the Name field."),
        default=_("Your name")
    )
    email_label = models.CharField(
        _("email"),
        max_length=250,
        help_text=_("Label for the e-mail field."),
        default=_("Your e-mail")
    )
    message_label = models.CharField(
        _("message"),
        max_length=250,
        help_text=_("Label for the Message field."),
        default=_("Message")
    )

    # Form settings
    success_msg = RichTextField(
        _("success message"),
        default=_("Message sent, thanks for contacting us!")
    )
    to_address = models.EmailField(
        _("to address"),
        blank=True, null=True,
        help_text=_("E-mail to notify when a new submission is received. Leave"
                    " it empty to disable the notifications.")
    )
    notification_subject = models.CharField(
        _("subject"),
        blank=True, null=True,
        max_length=250,
        help_text=_("If empty, you will not get e-mail notifications for new "
                    "form submissions.")
    )

    field_labels = [
        FieldPanel('name_label', classname="full"),
        FieldPanel('email_label', classname="full"),
        FieldPanel('message_label', classname="full"),
    ]
    form_settings = [
        FieldPanel('success_msg', classname="full"),
        FieldPanel('to_address', classname="full"),
        FieldPanel('notification_subject', classname="full"),
    ]

    content_panels = BasePage.content_panels + [
        MultiFieldPanel(
            field_labels,
            heading=_("Field labels"),
        ),
        MultiFieldPanel(
            form_settings,
            heading=_("Form settings"),
        ),
    ]

    def serve(self, request, *args, **kwargs):
        # as request.is_ajax() is deprecated, checking HTTP_X_REQUESTED_WITH
        if (
            request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
            and request.method == 'POST'
        ):
            form_class = self.get_contact_form()
            post_from_fetch = json.loads(request.body)
            form = form_class(post_from_fetch)
            if form.is_valid():
                if self.to_address and self.notification_subject:
                    form.send_submission_notification(
                        self.to_address, self.notification_subject,
                        post_from_fetch
                    )

                # Receipt: disabled for now.
                # form.send_submission_receipt()

                submissions_model = self.get_submissions_model()
                if submissions_model:
                    form.save()

                success_return_data = {
                    'success': True
                }
                return JsonResponse(success_return_data)
            else:
                return JsonResponse({
                    'errors': form.errors
                })

        return super().serve(request, *args, **kwargs)

    @staticmethod
    def get_contact_form():
        from .forms import ContactUsForm
        return ContactUsForm

    @staticmethod
    def get_submissions_model():
        return ContactSubmission


class ContactSubmission(models.Model):
    class Meta:
        verbose_name = _("contact form submission")
        verbose_name_plural = _("contact form submissions")

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        _("name"),
        max_length=120,
    )
    email = models.EmailField(
        _("e-mail"),
        max_length=255,
    )
    message = models.TextField(
        _("message"),
    )

    def __str__(self):
        return f"{self.name} ({self.email}) on {self.created}"
