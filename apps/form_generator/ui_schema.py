from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Any, Dict

from apps.form_generator.ui_type.base import FormUnit


@dataclass
class VueFormUnit(FormUnit):
    type: str = field(init=False)
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    outer_class: List[str] = field(default_factory=list)
    extra_option: Dict[str, Any] = field(default_factory=dict)


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
