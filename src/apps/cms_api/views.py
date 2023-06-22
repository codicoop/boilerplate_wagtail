from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from apps.cms_api.serializers import (
    CollectionItemReadSerializer,
    HistoryItemReadSerializer,
    VideoItemReadSerializer,
)
from apps.cms_site.models import CollectionItem
from apps.cms_site.models.about_us import HistoryItem, VideoItem


class CollectionItemViewSet(
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


class VideoItemViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = VideoItem.objects.all()
    serializer_class = VideoItemReadSerializer
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = [
        "page",
    ]


class HistoryItemViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = HistoryItem.objects.all()
    serializer_class = HistoryItemReadSerializer
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = [
        "page",
    ]
