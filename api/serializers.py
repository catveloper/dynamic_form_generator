from django.contrib.auth.models import User, Group
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample, extend_schema_field
from rest_framework import serializers


@extend_schema_serializer(
    exclude_fields=["password", "email"],
    deprecate_fields=["url"],
    examples=[
        OpenApiExample(
            "Valid example 1",
            summary="short summary",
            description="longer description",
            value={
                "Example"
            },
            request_only=True,
        ),
    ],
    component_name='CU'
)
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    field_custom = serializers.SerializerMethodField(method_name="get_field_custom")

    class Meta:
        model = User
        fields = '__all__'

    @extend_schema_field(OpenApiTypes.DATETIME)
    def get_field_custom(self, data):
        return '2021-03-06 20:54:00'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class VueFormulateSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    form_generator = []