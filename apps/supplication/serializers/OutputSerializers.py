from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import supplication


class supplicationSerializer(ModelSerializer):
    class Meta:
        model = supplication
        fields = (
            "uuid",
            "supplication_content",
        )
