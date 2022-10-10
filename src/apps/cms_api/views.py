from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from apps.cms_api.serializers import CollectionItemReadSerializer
from apps.cms_site.models import CollectionItem


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
