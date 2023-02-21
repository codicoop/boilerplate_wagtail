from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.options import ModelAdmin

from .models import ContactSubmission


class ValidationPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        return False

    def user_can_edit_obj(self, user, obj):
        return False

    def user_can_delete_obj(self, user, obj):
        return False


class ContactSubmissionAdmin(ModelAdmin):
    permission_helper_class = ValidationPermissionHelper
    model = ContactSubmission
    # ditch this to use verbose_name_plural from model
    # Translators: This is for Wagtail's admin menu, keep it very short.
    menu_label = _("Form submissions")
    menu_icon = 'mail'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    # or True to add your model to the Settings sub-menu
    add_to_settings_menu = False
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = True
    list_display = ('created', 'name', 'email', 'message', )
    list_filter = ('created', )
    search_fields = ('name', 'email', 'message', )
    edit_view_class = None

# Only register it if you are using the original. If you are using a diferent
# setr of fields, you might want to define or extend a different ModelAdmin
# somewhere else and register your version.
# modeladmin_register(ContactSubmissionAdmin)
