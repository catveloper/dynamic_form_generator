import copy
from enum import Enum, EnumMeta

from apps.form_generator.ui_type import vue_formulator, react
from apps.form_generator.ui_type.base import BaseFormUnit


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
    VUE_FORMULATOR = ('vue_formulator', )
    REACT = ('react', )

    def __init__(self, view_name: str):
        self.view_name = view_name


class Widget(CustomEnum):
    INPUT = ('text', vue_formulator.Input, react.Input)
    TEXT_AREA = ('textarea', vue_formulator.TextArea, react.TextArea)
    SELECT = ('select', vue_formulator.Select, react.Select)
    CHECK_BOX = ('check_box', vue_formulator.CheckBox, react.CheckBox)

    def __init__(self, ui_name: str, *args):
        self.ui_name = ui_name
        for idx, ui_type in enumerate(UIType):
            setattr(self, ui_type.name, args[idx])

    def __call__(self, name=None, label=None, value=None, **keywords):
        if keywords:
            pass
        return BaseFormUnit(self, name, label, value, **keywords)

    def __getitem__(self, key):
        if isinstance(key, str):
            result = getattr(self, key)
        elif isinstance(key, UIType):
            result = getattr(self, key.name)
        else:
            raise TypeError("Key is 'str' or 'UIType'!!")

        if not result:
            raise AttributeError('Not matched key')

        return result
