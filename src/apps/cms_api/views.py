from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from apps.cms_api.serializers import (
    CollectionItemReadSerializer,
    HistoryItemReadSerializer,
    InstagramPostReadSerializer,
    VideoItemReadSerializer,
)
from apps.cms_site.models import CollectionItem
from apps.cms_site.models.about_us import HistoryItem, VideoItem
from apps.cms_site.models.news import InstagramPost


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


class HistoryItemViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = HistoryItem.objects.all()
    serializer_class = HistoryItemReadSerializer


class InstagramPostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = InstagramPost.objects.all()
    serializer_class = InstagramPostReadSerializer
