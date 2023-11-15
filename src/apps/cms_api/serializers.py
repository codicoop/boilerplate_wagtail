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
    finishings = serializers.SerializerMethodField()
    typologies = serializers.SerializerMethodField()
    image_thumbnail = ImageRenditionField("width-700", source="image")
    image_maximized = ImageRenditionField("width-1500", source="image")
    model = serializers.StringRelatedField()

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

    def get_finishings(self, obj):
        data = []
        try:
            translated_finishings = [
                finishing.get_translation(obj.locale)
                for finishing in obj.finishings.all()
            ]
        except CollectionItemFinishing.DoesNotExist:
            return data
        finishing_serializer = CollectionItemFinishingSerializer(
            translated_finishings,
            many=True,
            read_only=True
        )
        data = finishing_serializer.data
        return data

    def get_typologies(self, obj):
        data = []
        try:
            translated_typologies = [
                finishing.get_translation(obj.locale)
                for finishing in obj.typologies.all()
            ]
        except CollectionItemType.DoesNotExist:
            return data
        typology_serializer = CollectionItemTypeSerializer(
            translated_typologies,
            many=True,
            read_only=True
        )
        data = typology_serializer.data
        return data


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
