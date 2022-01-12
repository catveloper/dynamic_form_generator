import json

from drf_spectacular.generators import EndpointEnumerator
from setuptools import find_packages

from form_schema_generator.convertors.base import UISchemaConvertor
from form_schema_generator.enums import UIType
from form_schema_generator.generator import UISchemaGenerator, get_schema


packages = find_packages()
endpoints = EndpointEnumerator().get_api_endpoints()
serializer = UISchemaGenerator().get_serializer_by_endpoint("/api/tasks/", 'POST')
json_schema = get_schema(serializer)
ui_schema = UISchemaConvertor().convert(json_schema)
form_schema = UIType.VueFormulate.convertor.convert(ui_schema)
form_json_schema = json.dumps(form_schema, indent=4, ensure_ascii=False)
print(form_json_schema)