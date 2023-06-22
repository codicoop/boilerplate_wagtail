from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from wagtail.models import Locale

from apps.cms_api.serializers import (
    CollectionItemReadSerializer,
    HistoryItemReadSerializer,
    VideoItemReadSerializer,
)
from apps.cms_site.models import CollectionItem
from apps.cms_site.models.about_us import HistoryItem, VideoItem


class LanguageMixin(object):
    lookup_url_kwarg = "language"
    locale = None

    def get_queryset(self):
        queryset = super().get_queryset()
        language = self.kwargs.get(self.lookup_url_kwarg)
        if not language or language not in ["ca", "es"]:
            raise Http404()
        self.locale = Locale.objects.get(language_code=language)
        return queryset


class CollectionItemViewSet(
    # LanguageMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = CollectionItem.objects.all()
    serializer_class = CollectionItemReadSerializer
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = [
        "page",
        "model",
        "finishings",
        "typologies",
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(page__locale=self.locale)
        return queryset


class VideoItemViewSet(
    LanguageMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = VideoItem.objects.all()
    serializer_class = VideoItemReadSerializer


class HistoryItemViewSet(
    LanguageMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = HistoryItem.objects.all()
    serializer_class = HistoryItemReadSerializer
