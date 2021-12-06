from drf_spectacular.openapi import *
from rest_framework.serializers import Serializer


class CustomAutoSchema(AutoSchema):

    def _map_serializer_field(self, field, direction, bypass_extensions=False):
        result = super()._map_serializer_field(field, direction, bypass_extensions)
        meta = self._get_serializer_field_meta(field)

        if is_list_serializer(field) and is_serializer(field.child):
            component = self.resolve_serializer(field.child, direction)
            result = append_meta(build_array_type(component.schema), meta) if component else None
        elif is_serializer(field):
            component = self.resolve_serializer(field, direction)
            result = append_meta(component.schema, meta) if component else None

        return result


def get_schema(serializer_class: Serializer):
    serializer = force_instance(serializer_class)
    auto_schema = CustomAutoSchema()
    auto_schema.registry = ComponentRegistry()
    component = auto_schema.resolve_serializer(serializer, direction='request')
    return getattr(component, 'schema', None)