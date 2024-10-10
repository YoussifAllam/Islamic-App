from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets
from .serializers import OutputSerializers
from rest_framework.decorators import action
from .db_queries import selectors
from rest_framework.status import HTTP_200_OK


class AzkarCategoriesViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=["get"])
    def get_azkar_categories(self, request: Request) -> Response:
        categories = selectors.get_all_azkar_categories()
        serializer = OutputSerializers.AzkarCategoriesSerializer(categories, many=True)
        return Response({
            'status': 'success',
            'data': serializer.data}, status=HTTP_200_OK
        )


class AzkarViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["get"])
    def get_azkar_by_category(self, request: Request) -> Response:
        Response_data, Response_status = selectors.get_azkar_by_category(request)
        return Response(Response_data, status=Response_status)
