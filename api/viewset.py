from urllib.request import Request

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpRequest
from drf_spectacular.generators import SchemaGenerator
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer, CustomUserSerializer
from apps.form_generator.enums import Widget
from apps.form_generator.decorators import form_generate_view


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=['테스트'],
        description='테스트를 위한 메소드입니다',
        responses=GroupSerializer,
        examples=[
            OpenApiExample(
                response_only=True,
                summary="이거는 Response Body Example입니다.",
                name="success_example",
                value={
                    "url": "https://dashboard.datamaker.io/",
                    "name": "데이터메이커",
                },
            ),
        ],
        parameters=[
            OpenApiParameter(
                name="path_param",
                type=str,
                location=OpenApiParameter.PATH,
                description="아이디 입니다.",
                required=True,
            ),
            OpenApiParameter(
                name="text_param",
                type=str,
                description="text_param 입니다.",
                required=False,
            ),
            OpenApiParameter(
                name="select_param",
                type=str,
                description="first_param 입니다.",
                enum=['선택1', '선택2', '선택3'],
                examples=[
                    OpenApiExample(
                        name="이것은 Select Parameter Example입니다.",
                        summary="요약입니다",
                        description="설명글은 길게 작성합니다",
                        value="선택1",
                    ),
                    OpenApiExample(
                        "이것은 Query Parameter Example2입니다.",
                        summary="두번째 요약입니다",
                        description="두번째 설명글은 더 길게 작성합니다",
                        value="선택4",
                    ),
                ],
            ),
            OpenApiParameter(
                name="date_param",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="date filter",
                examples=[
                    OpenApiExample(
                        name="이것은 Query Parameter Example입니다.",
                        summary="요약입니다",
                        description="설명글은 길게 작성합니다",
                        value="1991-03-02",
                    ),
                    OpenApiExample(
                        name="이것은 Query Parameter Example2입니다.",
                        summary="두번째 요약입니다",
                        description="두번째 설명글은 더 길게 작성합니다",
                        value="1993-08-30",
                    ),
                ],
            ),
        ],
    )
    @action(
        detail=False
    )
    def test(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return Response(SchemaGenerator().get_schema())


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]