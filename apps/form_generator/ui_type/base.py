from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field
from typing import Optional, Dict, Any, List


class FormUnit(ABC):
    def get_schema(self):
        return asdict(self)

    @abstractmethod
    def convert_of(self, schema):
        pass


@dataclass(init=False)
class BaseFormUnit(FormUnit):
    widget: Any
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    extra_options: Dict[str, str] = field(default_factory=dict)

    def __init__(self, widget, name=None, label=None, value=None, **extra_options):
        self.widget = widget
        self.name = name
        self.label = label
        self.value = value
        self.extra_options = extra_options

    def get_schema(self):
        schema = asdict(self)
        schema.pop('extra_options')
        for k, v in self.extra_options.items():
            if k not in schema.keys():
                schema[k] = v
        return schema

    def convert_of(self, schema):
        pass
