from ..models import Azkar_categories
from ..serializers import ParamsSerializers, OutputSerializers
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


def get_all_azkar_categories() -> Azkar_categories:
    return Azkar_categories.objects.all()


def get_azkar_by_category(request: Request) -> tuple[dict[str, int]]:
    paramsSerializers = ParamsSerializers.AzkersParamsSerializer(
        data=request.GET, context={'request': request}
    )
    if not paramsSerializers.is_valid():
        return (
            {"status": "error", "error": paramsSerializers.errors},
            HTTP_400_BAD_REQUEST
        )

    category_uuid = paramsSerializers.validated_data["category_uuid"]
    category_obj = Azkar_categories.objects.get(uuid=category_uuid)
    Azkar = category_obj.Azkar_set
    Azkar_serializer = OutputSerializers.ZikrSerializer(Azkar, many=True)
    return (
        {'status': 'success', "data": Azkar_serializer.data},
        HTTP_200_OK
    )
