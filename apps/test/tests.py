from pprint import pp

from api.formulate import TestForm
from api.serializers import TaskSerializer
from apps.form_generator import generator

# Create your tests here.

pp({
    'schema': TestForm().get_serializer_schema(),
    'ui schema': TestForm().get_ui_schema()
})
