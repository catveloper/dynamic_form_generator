from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.test.models import Task, Annotation, Project


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
        depth = 1
