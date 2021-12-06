from django.contrib.auth.models import User, Group
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample, extend_schema_field
from rest_framework import serializers

from apps.test.models import Task, Annotation, Project


class CustomUserSerializer(serializers.ModelSerializer):
    field_custom = serializers.SerializerMethodField(method_name="get_field_custom")

    @extend_schema_field(OpenApiTypes.DATETIME)
    def get_field_custom(self, data):
        return '2021-03-06 20:54:00'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    annotations = AnnotationSerializer(many=True)
    project = ProjectSerializer()

    class Meta:
        model = Task
        fields = ['name', 'annotations', 'project']
