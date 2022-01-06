from rest_framework import serializers

from apps.form_schema_generator.enums import UIType, HttpMethod


class FormGeneratorSerializer(serializers.Serializer):
    url = serializers.ChoiceField(choices=[],)
    method = serializers.ChoiceField(choices=HttpMethod.choices)
    type = serializers.ChoiceField(choices=UIType.choices)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate_url(self):
        pass

    @classmethod
    def get_declared_field_choices(cls, field_name):
        field = cls._declared_fields.get(field_name)
        choices = getattr(field, 'choices')
        return choices



