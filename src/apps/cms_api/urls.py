from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.cms_api.views import CollectionItemViewSet, HistoryItemsList, \
    VideoItemViewSet, HistoryItemViewSet

router = DefaultRouter()
router.register(
    r"collection_items",
    CollectionItemViewSet,
    basename="collection_item",
)
router.register(
    r"video_items",
    VideoItemViewSet,
    basename="video_item",
)
router.register(
    r"history_items",
    HistoryItemViewSet,
    basename="history_item",
)

urlpatterns = router.urls
