from django.http import HttpRequest, HttpResponse
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import *

from api.serializers import UserSerializer
from apps.form_generator import generator
from apps.form_generator.serializers import FormGeneratorSerializer


class FormulatorAPI(GenericViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = FormGeneratorSerializer

    @extend_schema(
        description='form-generator proxy API',
        parameters=[
            OpenApiParameter(
                name="alias",
                required=True,
                description="form-ui에 대한 별칭입니다",
                enum=serializer_class._declared_fields['alias'].choices,
            ),
            OpenApiParameter(
                name="type",
                required=True,
                description="form-ui-schema가 생성될 타입입니다",
                enum=serializer_class._declared_fields['type'].choices
            ),
        ],
    )
    @action(detail=False, methods=['get'], url_path='form-generator', url_name='form_generator')
    def generator(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        serializer = FormGeneratorSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        schema = generator.get_schema(UserSerializer)
        return Response(schema, status=status.HTTP_200_OK)

    def get_form_class(self, alias):
        # 캐싱된 항목들에서 alias로 대상을 불러온다 , 혹시 다른 더 좋은 방법이 있다면 그렇게 진행
        pass

    def convert(self, alias: str, type: str):
        # 타입에 따라 다른 UI schema로변환한다
        pass


