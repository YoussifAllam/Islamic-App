from ..serializers import OutputSerializers
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from .. models import supplication


def get_all_supplication(request: Request) -> tuple[dict[str, int]]:
    supplication_objs = supplication.objects.all()
    serializer = OutputSerializers.supplicationSerializer(supplication_objs, many=True)
    return (
        {'status': 'success', "data": serializer.data},
        HTTP_200_OK
    )
