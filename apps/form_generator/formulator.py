# TODO: 하나의 serializer로  여러 form을 만들 수 있도록
# TODO: serializer의 필드들에 대응되는 디폴트 필드 정의
# TODO: @데코레이터 또는 상속관계 활용해서 formulator에서 사용가능한 항목들 캐싱
# TODO: 폼 제네레이터를 하나의 패키지화 시켜서 어디서든 적용가능하도록
# TODO: url커스텀이 가능하도록
from collections import OrderedDict
from typing import Dict, Any

from rest_framework.serializers import ModelSerializer
from rest_framework.utils import model_meta

from apps.form_generator.enums import Widget
from apps.form_generator.generator import get_schema
from apps.form_generator.ui_type.base import BaseFormUnit, FormUnit

formulators: Dict[str, Any] = {}


def get_all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in get_all_subclasses(c)])


def set_new_attribute(cls, name, value):
    # Never overwrites an existing attribute.  Returns True if the
    # attribute already exists.
    if name in cls.__dict__:
        return True
    setattr(cls, name, value)
    return False


def get_label(serializer, field_name):
    if isinstance(serializer, ModelSerializer):
        model_class = serializer.Meta.model
        model_field_info = model_meta.get_field_info(model_class)
        field = model_field_info.fields.get(field_name)
        label = field.verbose_name if field else None
    else:
        return None

    return label


class FormulatorOptions:
    def __init__(self, options=None):
        self.alias = getattr(options, 'alias', None)
        self.serializer = getattr(options, 'serializer', None)


class FormulatorMeta(type):

    @classmethod
    def _get_declared_fields(mcs, bases, attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, FormUnit) or isinstance(type(obj), mcs)]

        # Ensures a base class field doesn't override cls attrs, and maintains
        # field precedence when inheriting multiple parents. e.g. if there is a
        # class C(A, B), and A and B both define 'field', use 'field' from A.
        known = set(attrs)

        def visit(name):
            known.add(name)
            return name

        base_fields = [
            (visit(name), f)
            for base in bases if hasattr(base, '_declared_fields')
            for name, f in base._declared_fields.items() if name not in known
        ]

        return OrderedDict(base_fields + fields)

    @classmethod
    def _register_formulator(mcs, cls, alias):
        if alias in formulators.keys():
            raise Exception("alias is duplicated!! Check alias field or class name")

        formulators[alias] = cls

    @classmethod
    def _validate_fields(mcs, serializer, fileds):
        # TODO: 연관관계가 있는것만 formulator class 사용가능 , 아니면 에러
        # TODO: 필드 중에 name 과 label이 선언 안되어 있다면, 자동으로 선언

        pass

    def __new__(mcs, name, bases, attrs):
        attrs['_declared_fields'] = mcs._get_declared_fields(bases, attrs)
        new_class = super().__new__(mcs, name, bases, attrs)
        if len(bases) > 0:
            opts = new_class._meta = FormulatorOptions(getattr(new_class, 'Meta', None))
            alias = opts.alias or name
            mcs._register_formulator(new_class, alias)
        # mcs._validate_fields(new_class._meta.serializer, attrs['_declared_fields'])
        return new_class


class Formulator(metaclass=FormulatorMeta):

    def get_serializer_schema(self):
        return get_schema(self._meta.serializer) if self._meta.serializer else None

    def get_ui_schema(self, schema=None, name="", prefix=""):
        ui_schema = {}
        obj = self._declared_fields.get(name)
        prefix_name = "-".join([prefix, name]) if prefix and name else name

        if schema is None:
            schema = self.get_serializer_schema()
            ui_schema['type'] = 'object'
            properties = {}
            for pp_name, pp_schema in schema['properties'].items():
                properties[pp_name] = self.get_ui_schema(pp_schema, pp_name, prefix)

            for filed_name, extra_field in self._declared_fields.items():
                if filed_name in properties.keys():
                    continue
                extra_field.name = extra_field.name or filed_name
                extra_field.label = extra_field.label or extra_field.name
                properties[filed_name] = extra_field.get_schema()

            properties = {
                p_info[0]: p_info[1]
                for p_info in sorted(properties.items(),
                key=lambda p: p[1].get('type', ''))
            }
            ui_schema['properties'] = properties


        elif isinstance(obj, Formulator):
            field_type = schema['type']

            if field_type == 'object':
                ui_schema = obj.get_ui_schema(prefix=prefix_name)
            elif field_type == 'array':
                ui_schema['type'] = field_type
                ui_schema['items'] = obj.get_ui_schema(prefix=prefix_name)

        elif isinstance(obj, FormUnit):
            obj.name = "-".join([prefix, prefix, obj.name]) if obj.name else prefix_name
            obj.label = obj.label or name
            ui_schema = obj.get_schema()

        else:
            # TODO schema의 형태에 따른 다른 default_ui (dictionary or enum 활용)
            default_ui = BaseFormUnit(Widget.INPUT, prefix_name, name)
            ui_schema = default_ui.get_schema()

        return ui_schema
