from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField

from apps.cms_site.models import CollectionItem, CollectionItemFinishing, \
    CollectionItemType


class CollectionItemFinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItemFinishing
        fields = [
            "id",
            "title",
        ]


class CollectionItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItemType
        fields = [
            "id",
            "title",
        ]


class CollectionItemReadSerializer(serializers.ModelSerializer):
    finishings = CollectionItemFinishingSerializer(
        many=True,
        read_only=True,
    )
    typologies = CollectionItemTypeSerializer(
        many=True,
        read_only=True,
    )
    image_thumbnail = ImageRenditionField("width-700", source="image")
    image_maximized = ImageRenditionField("width-1500", source="image")

    class Meta:
        model = CollectionItem
        fields = [
            "id",
            "title",
            "image_thumbnail",
            "image_maximized",
            "model",
            "finishings",
            "typologies",
        ]
