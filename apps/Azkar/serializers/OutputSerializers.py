from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import Zikr, Azkar_categories


class AzkarCategoriesSerializer(ModelSerializer):
    class Meta:
        model = Azkar_categories
        fields = (
            "uuid",
            "name",
            "icon",
        )


class ZikrSerializer(ModelSerializer):
    class Meta:
        model = Zikr
        fields = (
            "uuid",
            "zikr_category",
            "zikr_content",
            "zikr_repetitions",
        )
