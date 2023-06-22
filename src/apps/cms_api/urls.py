from rest_framework.routers import DefaultRouter

from apps.cms_api.views import (
    CollectionItemViewSet,
    HistoryItemViewSet,
    VideoItemViewSet,
)

router = DefaultRouter()
router.register(
    r"collection_items",
    CollectionItemViewSet,
    basename="collection_item",
)
router.register(
    r"video_items/<str:language>/",
    VideoItemViewSet,
    basename="video_item",
)
router.register(
    r"history_items/<str:language>/",
    HistoryItemViewSet,
    basename="history_item",
)

urlpatterns = router.urls
