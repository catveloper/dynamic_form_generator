from django.contrib.auth.models import User, Group
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample, extend_schema_field
from rest_framework import serializers

from apps.form_generator.enums import UIType
from apps.form_generator.formulator import formulators


class FormGeneratorSerializer(serializers.Serializer):
    alias = serializers.ChoiceField(choices=list(formulators.keys()))
    type = serializers.ChoiceField(choices=UIType.choices)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

