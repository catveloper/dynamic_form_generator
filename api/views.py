from urllib.request import Request

from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_http_methods
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer
from apps.form_generator.autoform import Input
from apps.form_generator.generator import form_generate


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


@form_generate(
    form_units=[
        Input(name='name', label='이름'),
        Input(name='email', label='이메일'),
        Input(name='password', label='암호')
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
