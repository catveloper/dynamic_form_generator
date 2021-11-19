from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Any


@dataclass
class Component(ABC):
    component: str = 'div'
    clazz: Optional[str] = None
    children: List[Any] = field(default_factory=list)


@dataclass
class FormUnit(ABC):
    type: str = field(init=False)
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    outer_class: List[str] = field(default_factory=list)
    # TODO:확장옵션들도 맵형식으로 추가

    def get_form_schema(self):
        return asdict(self)


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
