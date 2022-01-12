from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import MultipleChoiceField

from apps.test.models import Task, Annotation, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'is_staff']


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
    name = MultipleChoiceField(choices=[('Back-end', '백엔드개발자'), ('PM', '프로젝트 관리자'), ('Front-end', '프론트엔드 개발자'), ('machine-learning', 'AI 개발자')])
    project = ProjectSerializer(label='프로젝트')
    annotations = AnnotationSerializer(label='어노테이션들', many=True)

    class Meta:
        verbose_name = '테스크1'
        model = Task
        fields = ['id', 'name', 'project', 'annotations']
        depth = 1
