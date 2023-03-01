from rest_framework.routers import DefaultRouter

from apps.cms_api.views import (
    CollectionItemViewSet,
    HistoryItemViewSet,
    InstagramPostViewSet,
    VideoItemViewSet,
)

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
router.register(
    r"instagram_posts",
    InstagramPostViewSet,
    basename="instagram_post",
)

urlpatterns = router.urls
