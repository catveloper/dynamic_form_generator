from importlib import import_module

from django.apps import AppConfig
from django.utils.module_loading import module_has_submodule


SEARCH_MODULE_NAME = 'formulate'


class FormGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.form_generator'

    def ready(self):
        from django.apps import apps

        for app_config in apps.app_configs.values():
            if module_has_submodule(app_config.module, SEARCH_MODULE_NAME):
                module_name = f'{app_config.name}.{SEARCH_MODULE_NAME}'
                import_module(module_name)

