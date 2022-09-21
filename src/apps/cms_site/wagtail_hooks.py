from wagtail import hooks
from wagtail.images.models import Image
from wagtail.models import Collection

from apps.cms_site.models import CustomProject


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
