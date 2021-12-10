from pprint import pp

from api.formulate import TaskForm
# Create your tests here.
from api.serializers import TaskSerializer
from apps.form_generator.enums import Widget, UIType
from apps.form_generator.generator import get_schema

serializer_schema = get_schema(TaskSerializer)
pp(serializer_schema)
ui_schema = TaskForm().get_ui_schema()
pp(ui_schema)


def convert(schema: dict, ui_type: UIType, name=None):
    converted = []
    field_type = schema.get('type')
    # nested object
    if field_type == 'object' and schema.get('properties'):
        if name:
            label = {
                'component': 'h3',
                'children': name
            }
            converted.append(label)
        for p_name, p_schema in schema['properties'].items():
            converted.extend(convert(p_schema, ui_type, p_name))
    # nested object array
    elif field_type == 'array':
        label = {
            'component': 'h3',
            'children': name
        }
        group = {
            'type': 'group',
            'name': name,
            'repeatable': True,
            'children': convert(schema['items'], ui_type)
        }
        converted.append(label)
        converted.append(group)
    else:
        widget = schema['widget'] if isinstance(schema['widget'], Widget) else Widget[schema['widget']]
        converted.append(widget[ui_type]().convert_of(schema).get_schema())
    return converted


def convert_by_component(schema: dict, ui_type: UIType):
    converted = {}
    field_type = schema.get('type')
    # nested object
    if field_type == 'object' and schema.get('properties'):
        for p_name, p_schema in schema['properties'].items():
            converted[p_name] = convert_by_component(p_schema, ui_type)
    # nested object array
    elif field_type == 'array':
        converted = convert_by_component(schema['items'], ui_type)
    else:
        widget = schema['widget'] if isinstance(schema['widget'], Widget) else Widget[schema['widget']]
        converted = widget[ui_type]().convert_of(schema).get_schema()
    return converted


vue_ui_schema = convert(ui_schema, UIType.VUE_FORMULATOR, 'Task')
pp(vue_ui_schema)
