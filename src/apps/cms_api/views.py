from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cms_api.serializers import CollectionItemReadSerializer
from apps.cms_site.models import CollectionItem, AboutUsPage


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
