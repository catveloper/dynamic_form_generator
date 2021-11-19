from django.apps import AppConfig



class FormGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.form_generator'

    def ready(self):
        from . import formulatorform
        subclasses = formulatorform.get_all_subclasses(formulatorform.FormulatorForm)
        formulatorform.FormFactory.formulates.extend(subclasses)
        for cls in formulatorform.FormFactory.formulates:
            print(cls)



