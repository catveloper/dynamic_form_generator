import builtins
import json
from functools import wraps
from pprint import pp

from typing import List

from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.form_generator.autoform import FormUnit


class MissingType:
    pass


MISSING = MissingType


def _set_new_attribute(cls, name, value):
    # Never overwrites an existing attribute.  Returns True if the
    # attribute already exists.
    if name in cls.__dict__:
        return True
    setattr(cls, name, value)
    return False


def _create_fn(name, args, body, *, globals=None, locals=None,
               return_type=MISSING):
    # Note that we mutate locals when exec() is called.  Caller
    # beware!  The only callers are internal to this module, so no
    # worries about external callers.
    if locals is None:
        locals = {}
    if 'BUILTINS' not in locals:
        locals['BUILTINS'] = builtins
    return_annotation = ''
    if return_type is not MISSING:
        locals['_return_type'] = return_type
        return_annotation = '->_return_type'
    args = ','.join(args)
    body = '\n'.join(f'  {b}' for b in body)

    # Compute the text of the entire function.
    txt = f' def {name}({args}){return_annotation}:\n{body}'

    local_vars = ', '.join(locals.keys())
    txt = f"def __create_fn__({local_vars}):\n{txt}\n return {name}"

    ns = {}
    exec(txt, globals, ns)
    return ns['__create_fn__'](**locals)


def form_generate(form_units: List[FormUnit] = []):
    """
        document
    """

    def decorator(cls: APIView = None):
        @action(detail=False, methods=['get'])
        def form_schema(self: GenericAPIView, request: HttpRequest) -> HttpResponse:
            form = []
            for form_unit in form_units:
                form.append(form_unit.get_form_schema())
            form_str = json.dumps(form)
            pp(form_str)
            return Response(form)

        setattr(cls, 'form_schema', form_schema)
        return cls

    return decorator
