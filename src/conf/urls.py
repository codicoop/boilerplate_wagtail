"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls

from apps.cms_site.api import api_router

urlpatterns = [
    # Standard Django Admin URLs.
    path("admin/", admin.site.urls),
    path("cms/autocomplete/", include(autocomplete_admin_urls)),
    # The admin interface for Wagtail. This is separate from the Django admin
    # interface (django.contrib.admin); Wagtail-only projects typically host
    # the Wagtail admin at /admin/, but if this would clash with your project’s
    # existing admin backend then an alternative path can be used, such as
    # /cms/ here.
    path("cms/", include(wagtailadmin_urls)),
    # The location from where document files will be served. This can be
    # omitted if you do not intend to use Wagtail’s document management
    # features.
    path("documents/", include(wagtaildocs_urls)),
    path('api/v2/', api_router.urls),
]

urlpatterns += i18n_patterns(
    # The base location from where the pages of your Wagtail site will be
    # served. This was originally set as '/pages/',
    # leaving the root URL and other paths to be handled as normal by your
    # Django project. As we want Wagtail to handle the entire URL space
    # including the root URL, this can got replaced with:
    # path('', include(wagtail_urls)),
    #
    # This should be placed at the end of the urlpatterns list,
    # so that it does not override more specific URL patterns.
    path("", include(wagtail_urls)),
)
