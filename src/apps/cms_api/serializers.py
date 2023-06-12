from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField

from apps.cms_site.models import (
    CollectionItem,
    CollectionItemFinishing,
    CollectionItemType,
)
from apps.cms_site.models.about_us import HistoryItem, VideoItem


class CollectionItemFinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItemFinishing
        fields = [
            "id",
            "name",
        ]


class CollectionItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItemType
        fields = [
            "id",
            "name",
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
    title = serializers.SerializerMethodField(method_name="get_title")

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

    def get_title(self, obj):
        # To Do: return the right one according to language.
        return obj.title_ca


class VideoItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItem
        fields = [
            "id",
            "title",
            "embed",
            "description",
        ]


class HistoryItemReadSerializer(serializers.ModelSerializer):
    image_thumbnail = ImageRenditionField("width-700", source="image")
    image_maximized = ImageRenditionField("width-1500", source="image")

    class Meta:
        model = HistoryItem
        fields = [
            "id",
            "year",
            "title",
            "description",
            "image_thumbnail",
            "image_maximized",
        ]
