# Create your views here.
from django.views.generic import TemplateView


class StaticGenerateFV(TemplateView):
    template_name = 'form_generator/static_generate_view.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['api_form_schema'] = self.get_api_form_schema(kwargs['view_type'])
    #     return context_data
    #
    # def get_api_form_schema(self, view_type):
    #     serializer = FormGeneratorSerializer
    #     json_schema = get_schema(serializer)
    #     ui_schema = UISchemaConvertor().convert(json_schema)
    #     form_schema = UIType[view_type].convertor.convert(ui_schema)
    #
    #     return form_schema