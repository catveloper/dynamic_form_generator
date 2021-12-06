from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Any, Dict

from apps.form_generator.ui_type.base import FormUnit


# TODO: base ui_class 로 부터 vueformulator 형식의 schema 를 도출
def toVueFormulatorSchema(form_cls):
    pass


@dataclass
class VueFormUnit(FormUnit):
    type: str = field(init=False)
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    extra_option: Dict[str, str] = field(default_factory=dict)


@dataclass
class Input(FormUnit):
    type: str = 'text'
    placeholder: Optional[str] = None


@dataclass
class TextArea(FormUnit):
    type: str = 'textarea'


@dataclass
class Select(FormUnit):
    type: str = 'select'
    placeholder: Optional[str] = None
    options: dict = field(default_factory=dict)


@dataclass
class CheckBox(FormUnit):
    type: str = 'checkbox'
    options: dict = field(default_factory=dict)
