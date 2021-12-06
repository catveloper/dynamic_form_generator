import copy
from enum import Enum, EnumMeta
from typing import Type

from apps.form_generator.ui_type import vue_formulator,react
from apps.form_generator.ui_type.base import FormUnit, BaseFormUnit


class CustomEnumMeta(EnumMeta):

    @property
    def choices(cls):
        return [(instance.name, instance.value[0]) for instance in cls]

    def to_dict(cls):
        result: dict = {}
        for instance in cls:
            instance_info: dict = copy.deepcopy(instance.__dict__)
            del instance_info['__objclass__']
            result[instance.name] = instance_info
        return result


class CustomEnum(Enum, metaclass=CustomEnumMeta):
    pass


class UIType(CustomEnum):
    VUE = ('vue_formulate',)
    REACT = ('react',)

    def __init__(self, view_name: str):
        self.view_name = view_name


class Widget(CustomEnum):
    INPUT = ('text',)
    TEXT_AREA = ('textarea', )
    SELECT = ('select', )
    CHECK_BOX = ('check_box', )

    def __init__(self, ui_name: str, ):
        self.ui_name = ui_name

    def __repr__(self):
        return self.name

    def __call__(self, name=None, label=None, value=None, **keywords):

        return BaseFormUnit(name, label, value, keywords)

    def get_by_ui_type(self, type_name):
        pass