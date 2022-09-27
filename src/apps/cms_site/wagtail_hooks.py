from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, \
    modeladmin_register
from wagtail.images.models import Image
from wagtail.models import Collection

from apps.cms_site.models import CustomProject, CollectionItemFinishing, \
    CollectionItemType
from apps.cms_site.models.snippets import CollectionItemModel
from django.utils.translation import gettext_lazy as _


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


class FinishingsModelAdmin(ModelAdmin):
    model = CollectionItemFinishing
    menu_label = _("Finishings")
    menu_icon = "plus-inverse"
    list_display = ("name", )
    search_fields = ("name", )
    inspect_view_enabled = True


class CollectionItemTypeModelAdmin(ModelAdmin):
    model = CollectionItemType
    menu_label = _("Types")
    menu_icon = "plus-inverse"
    list_display = ("name", )
    search_fields = ("name", )
    inspect_view_enabled = True


class CollectionItemModelModelAdmin(ModelAdmin):
    model = CollectionItemModel
    menu_label = _("Models")
    menu_icon = "plus-inverse"
    list_display = ("name", )
    search_fields = ("name", )
    inspect_view_enabled = True


modeladmin_register(FinishingsModelAdmin)
modeladmin_register(CollectionItemTypeModelAdmin)
modeladmin_register(CollectionItemModelModelAdmin)
