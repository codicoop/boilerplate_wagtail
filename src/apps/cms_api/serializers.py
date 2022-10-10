from rest_framework import serializers

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

    class Meta:
        model = CollectionItem
        fields = [
            "id",
            "title",
            "image",
            "model",
            "finishings",
            "typologies",
        ]
