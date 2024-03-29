from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.contrib.modeladmin.options import modeladmin_register
from wagtail.images.models import Image
from wagtail.models import Collection
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from apps.cms_site.models import (
    CollectionItemFinishing,
    CollectionItemType,
    CustomProject,
)
from apps.cms_site.models.contact import AjaxContactSubmission
from apps.cms_site.models.snippets import CollectionItemModel
from apps.wagtail_ajax_contact_form.wagtail_hooks import ContactSubmissionAdmin


@hooks.register("after_delete_page")
def after_delete_custom_project(request, page):
    """Delete CustomProject's linked Collection."""

    if (
        request.method == "POST"
        and page.specific_class is CustomProject
        and page.images_collection
    ):
        Image.objects.filter(collection=page.images_collection).delete()
        Collection.objects.get(id=page.images_collection.id).delete()


class FinishingsModelAdmin(TranslatableModelAdmin):
    model = CollectionItemFinishing
    menu_label = _("Finishings")
    menu_icon = "plus-inverse"
    list_display = ("name",)
    search_fields = ("name",)
    inspect_view_enabled = True


class CollectionItemTypeModelAdmin(TranslatableModelAdmin):
    model = CollectionItemType
    menu_label = _("Types")
    menu_icon = "plus-inverse"
    list_display = ("name",)
    search_fields = ("name",)
    inspect_view_enabled = True


class CollectionItemModelModelAdmin(TranslatableModelAdmin):
    model = CollectionItemModel
    menu_label = _("Models")
    menu_icon = "plus-inverse"
    list_display = ("name",)
    search_fields = ("name",)
    inspect_view_enabled = True


class ContactAjaxSubmissionAdmin(ContactSubmissionAdmin):
    model = AjaxContactSubmission
    list_display = (
        "created",
        "name",
        "email",
        "message",
        "subject",
        "phone",
        "profile",
        "personal_data_auth",
        "personal_data_comercial_auth",
    )
    list_filter = (
        "created",
        "personal_data_auth",
        "personal_data_comercial_auth",
    )
    search_fields = (
        "name",
        "email",
        "message",
        "subject",
        "phone",
    )
    edit_view_class = None


modeladmin_register(FinishingsModelAdmin)
modeladmin_register(CollectionItemTypeModelAdmin)
modeladmin_register(CollectionItemModelModelAdmin)
modeladmin_register(ContactAjaxSubmissionAdmin)
