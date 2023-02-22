from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cms_api.serializers import CollectionItemReadSerializer, \
    VideoItemReadSerializer
from apps.cms_site.models import CollectionItem, AboutUsPage
from apps.cms_site.models.about_us import VideoItem


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


class HistoryItemsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        about_us = AboutUsPage.objects.first()
        serializer = about_us.history_items_list.stream_block.get_api_representation(
            about_us.history_items_list
        )
        return Response(serializer)
