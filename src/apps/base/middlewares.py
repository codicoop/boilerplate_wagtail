from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import get_language
from wagtail.models import Locale


class Redirect404to301Middleware(MiddlewareMixin):
    # Defined as class-level attributes to be subclassing-friendly.
    response_redirect_class = HttpResponsePermanentRedirect

    def process_response(self, request, response):
        # No need to check for a redirect for non-404 responses.
        # Root path queries fall into infinite redirection because it happens
        # before the localization URLs can redirect it to the specific
        # language path, like to /ca/.
        if response.status_code != 404 or request.get_full_path() == "/":
            return response

        return self.response_redirect_class("/")


class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_locale = Locale.objects.get(language_code=get_language())
        request.current_locale = current_locale
        response = self.get_response(request)
        return response
