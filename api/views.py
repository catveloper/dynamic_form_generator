from urllib.request import Request

from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_http_methods
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer
from apps.form_generator.autoform import Input
from apps.form_generator.enums import Form
from apps.form_generator.generator import form_generate_view


class StaticFormGeneratorAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request) -> Response:
        return Response(
            data=[
                {"type": "text", "name": "name", "label": None, "value": None, "outer_class": [], "placeholder": None},
                {"type": "text", "name": "email", "label": None, "value": None, "outer_class": [], "placeholder": None},
                {"type": "text", "name": "password", "label": None, "value": None, "outer_class": [],
                 "placeholder": None}]
        )


@form_generate_view(
    form_units=[
        Form.INPUT(name='name', label='이름', placeholder='이름을 입력하세요'),
        Form.INPUT(name='url', label='유알엘', placeholder='url을 입력하세요', value='www.nave.com'),
        Form.SELECT(name='email', label='이메일', placeholder='email을 입력하세요', options=['@naver.com', '@google.com', '@daum.net'])
    ]
)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # @action(detail=False, methods=['get'])
    # def schema(self, request: HttpRequest) -> HttpResponse:
    #     return Response(SchemaGenerator(url='/api/users').get_schema())


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
