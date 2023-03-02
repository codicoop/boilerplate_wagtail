from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


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
