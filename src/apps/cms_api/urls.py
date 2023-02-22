from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.cms_api.views import CollectionItemViewSet, HistoryItemsList, \
    VideoItemViewSet

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

urlpatterns = router.urls

urlpatterns += [
    path('history_items/', HistoryItemsList.as_view()),
]
