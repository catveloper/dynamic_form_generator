import json
from pprint import pp

from django.urls import reverse_lazy, reverse
from drf_spectacular.generators import EndpointEnumerator
from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer
from setuptools import find_packages
from typing import List

from form_schema_generator.convertors.base import UISchemaConvertor
from form_schema_generator.enums import UIType
from form_schema_generator.generator import UISchemaGenerator, get_schema
from form_schema_generator.serializers import FormGeneratorSerializer
from form_schema_generator.viewset import FormSchemaGeneratorAPI
