from rest_framework.routers import DefaultRouter

from apps.cms_api.views import CollectionItemViewSet

router = DefaultRouter()
router.register(
    r"collection_items",
    CollectionItemViewSet,
    basename="collection_item",
)

urlpatterns = router.urls
