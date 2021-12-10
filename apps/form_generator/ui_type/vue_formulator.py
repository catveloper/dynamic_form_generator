from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Any, Dict

from apps.form_generator.ui_type.base import FormUnit


@dataclass
class VueFormulatorFU(FormUnit):
    type: str = field(init=False)
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    extra_option: Dict[str, str] = field(default_factory=dict)

    def convert_of(self, schema):
        self.name = schema.get('name')
        self.label = schema.get('label')
        self.value = schema.get('value')
        return self


@dataclass
class Input(VueFormulatorFU):
    type: str = 'text'
    placeholder: Optional[str] = None

    def convert_of(self, schema):
        super().convert_of(schema)
        self.placeholder = schema.get('placeholder')
        return self


@dataclass
class TextArea(VueFormulatorFU):
    type: str = 'textarea'


@dataclass
class Select(VueFormulatorFU):
    type: str = 'select'
    placeholder: Optional[str] = None
    options: dict = field(default_factory=dict)

    def convert_of(self, schema):
        super().convert_of(schema)
        self.placeholder = schema.get('placeholder')
        self.options = schema.get('choices')
        return self


@dataclass
class CheckBox(VueFormulatorFU):
    type: str = 'checkbox'
    options: dict = field(default_factory=dict)

    def convert_of(self, schema):
        super().convert_of(schema)
        self.placeholder = schema.get('placeholder')
        return self

