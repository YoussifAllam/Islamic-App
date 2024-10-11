from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets
from rest_framework.decorators import action
from .db_queries import selectors


class supplicationViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["get"])
    def get_all_supplication(self, request: Request) -> Response:
        Response_data, Response_status = selectors.get_all_supplication(request)
        return Response(Response_data, status=Response_status)
