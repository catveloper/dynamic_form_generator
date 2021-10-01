from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Union, List, Optional, Any


@dataclass
class Component:
    component: str = 'div'
    clazz: Optional[str] = None
    children: List[Any] = field(default_factory=list)


@dataclass
class FormUnit:
    type: str = field(init=False)
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    outer_class: List[str] = field(default_factory=list)

    def get_form_schema(self):
        return asdict(self)


@dataclass
class Input(FormUnit):
    type: str = 'text'
    placeholder: str = None


@dataclass
class TextArea(FormUnit):
    type: str = 'textarea'


@dataclass
class Select(FormUnit):
    type: str = 'select'
    options: dict = field(default_factory=dict)


@dataclass
class CheckBox(FormUnit):
    type: str = 'checkbox'
    options: dict = field(default_factory=dict)
