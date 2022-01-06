from django.apps import AppConfig


class FormGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.form_schema_generator'

    def ready(self):
        from apps.form_schema_generator.generator import UISchemaGenerator

        def get_url_choices():
            schema_generator = UISchemaGenerator()
            endpoints = schema_generator.get_all_endpoints()
            return set([
                endpoint[0]
                for endpoint in endpoints
                if endpoint[2] in ['PUT', 'PATCH', 'POST']
            ])

        url_choices = get_url_choices()

        from .serializers import FormGeneratorSerializer
        url_choice_field = FormGeneratorSerializer._declared_fields['url']
        url_choice_field.choices = url_choices

