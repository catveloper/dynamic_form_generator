from abc import ABC, abstractmethod

from apps.form_generator.enums import UIType, Widget


class Convertor:
    @classmethod
    def convert(cls, schema: dict, ui_type, name=None):
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
                converted.extend(cls.convert(p_schema, ui_type, p_name))
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
                'children': cls.convert(schema['items'], ui_type)
            }
            converted.append(label)
            converted.append(group)
        else:
            widget = schema['widget'] if isinstance(schema['widget'], Widget) else Widget[schema['widget']]
            converted.append(widget[ui_type]().convert_of(schema).get_schema())
        return converted

    @classmethod
    def convert_by_field(cls, schema: dict, ui_type: UIType):
        converted = {}
        field_type = schema.get('type')
        # nested object
        if field_type == 'object' and schema.get('properties'):
            for p_name, p_schema in schema['properties'].items():
                converted[p_name] = cls.convert_by_component(p_schema, ui_type)
        # nested object array
        elif field_type == 'array':
            converted = cls.convert_by_component(schema['items'], ui_type)
        else:
            widget = schema['widget'] if isinstance(schema['widget'], Widget) else Widget[schema['widget']]
            converted = widget[ui_type]().convert_of(schema).get_schema()
        return converted
