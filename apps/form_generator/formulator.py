# TODO: 하나의 serializer로  여러 form을 만들 수 있도록
# TODO: serializer의 필드들에 대응되는 디폴트 필드 정의
# TODO: @데코레이터 또는 상속관계 활용해서 formulator에서 사용가능한 항목들 캐싱
# TODO: 폼 제네레이터를 하나의 패키지화 시켜서 어디서든 적용가능하도록
# TODO: url커스텀이 가능하도록
from collections import OrderedDict
from typing import Dict

from rest_framework.serializers import ModelSerializer
from rest_framework.utils import model_meta

from apps.form_generator.enums import Widget
from apps.form_generator.generator import get_schema
from apps.form_generator.ui_type.base import BaseFormUnit, FormUnit

formulators: Dict[str, object] = {}


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
    def _get_declared_fields(cls, bases, attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, FormUnit)]

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

    def __new__(mcs, name, bases, attrs):
        attrs['_declared_fields'] = mcs._get_declared_fields(bases, attrs)
        new_class = super().__new__(mcs, name, bases, attrs)

        if len(bases) > 0:
            # TODO: alias 가 있다면, alias를 따라서  없다면, class 네임으로 dictionary로 저장
            opts = new_class._meta = FormulatorOptions(getattr(new_class, 'Meta', None))
            alias = opts.alias or name
            mcs._register_formulator(new_class, alias)

        return new_class


class Formulator(metaclass=FormulatorMeta):

    def get_serializer_schema(self):
        return get_schema(self._meta.serializer) if self._meta.serializer else None

    def get_ui_schema(self, schema=None, name=None):
        # 일단 모든 항목을 input 으로 필드네임을 name으로 설정
        if schema is None:
            schema = self.get_serializer_schema()

        field_type = schema['type']
        ui_schema = {}
        if field_type == 'object' and schema.get('properties'):
            ui_schema['type'] = field_type
            ui_schema['properties'] = {}
            for p_name, p_schema in schema['properties'].items():
                ui_schema['properties'][p_name] = self.get_ui_schema(p_schema, p_name)

        elif field_type == 'array':
            ui_schema['type'] = field_type
            ui_schema['items'] = self.get_ui_schema(schema['items'], name)

        else:
            ui_schema = BaseFormUnit(Widget.INPUT, name, name).get_schema()

        return ui_schema
