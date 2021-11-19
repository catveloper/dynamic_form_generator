import builtins
import json
from functools import wraps
from pprint import pp

from typing import List

import typing
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.utils import model_meta
from rest_framework.views import APIView

from api.serializers import UserSerializer
from apps.form_generator.components import FormUnit
from apps.form_generator.enums import Form

DEFAULT_FORM_UNIT = Form.INPUT

def _set_new_attribute(cls, name, value):
    # Never overwrites an existing attribute.  Returns True if the
    # attribute already exists.
    if name in cls.__dict__:
        return True
    setattr(cls, name, value)
    return False


def form_generate_view(func_name: str = 'form_schema', form_units: List[FormUnit] = [], use_serializer: bool = True):
    """
        class 적용 decorator
    """

    def decorator(cls: APIView = None):
        @action(detail=False, methods=['get'])
        def form_schema(self: GenericAPIView, request: HttpRequest) -> HttpResponse:

            if use_serializer:
                serializer = self.get_serializer()
                declared_field_name = list(serializer.get_fields().keys())
                custom_field_names = list(form_unit.name for form_unit in form_units)
                default_form_field_names = list(set(declared_field_name).difference(custom_field_names))

                for field_name in default_form_field_names:
                    # TODO: Serializer META class 에 form 정보가 있다면 해당 정보로 바인딩
                    label = _get_label(serializer, field_name)
                    form_unit = DEFAULT_FORM_UNIT(name=field_name, label=label)
                    form_units.append(form_unit)

            schema = [form_unit.get_form_schema() for form_unit in form_units]
            return Response(schema)

        _set_new_attribute(cls, 'form_schema', form_schema)
        return cls

    return decorator


def _get_label(serializer, field_name):
    if isinstance(serializer, ModelSerializer):
        model_class = serializer.Meta.model
        model_field_info = model_meta.get_field_info(model_class)
        field = model_field_info.fields.get(field_name)
        label = field.verbose_name if field else None
    else:
        return None

    return label


# def form_generate(form_units: List[FormUnit] = []):
#     """
#         function 적용 decorator
#     """
#
#     def decorator(func):
#         @wraps(func)
#         def inner(self: GenericAPIView, request: HttpRequest) -> HttpResponse:
#             form = []
#
#             serializer: UserSerializer = self.serializer_class
#
#             for form_unit in form_units:
#                 form.append(form_unit.get_form_schema())
#             form_str = json.dumps(form)
#             pp(form_str)
#             return Response(form)
#
#         _set_new_attribute(cls, 'form_schema', form_schema)
#         return cls
#
#     return decorator
