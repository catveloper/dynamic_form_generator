import json

from drf_spectacular.generators import EndpointEnumerator

from apps.form_schema_generator.convertors import UiSchemaConvertor
from apps.form_schema_generator.enums import UIType
from apps.form_schema_generator.generator import UISchemaGenerator, get_schema

endpoints = EndpointEnumerator().get_api_endpoints()
serializer = UISchemaGenerator().get_serializer_by_endpoint("/api/tasks/{id}/", 'PUT')
json_schema = get_schema(serializer)
ui_schema = UiSchemaConvertor().convert(json_schema)
form_schema = UIType.VUE_JSF.convertor.convert(ui_schema)
form_json_schema = json.dumps(form_schema, indent=4, ensure_ascii=False)
print(form_json_schema)