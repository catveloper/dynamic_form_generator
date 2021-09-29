from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Union, List


@dataclass
class Component(ABC):
    component: str
    clazz: str
    children: Union[str, list]


@dataclass
class FormPiece:
    type: str = field(init=False)
    name: str = None
    label: str = None
    value: str = None
    outer_class: List[str] = field(default_factory=List)

    @property
    def type(self):
        return self.type or self.__class__.name.lower()

    def get_form_schema(self):
        asdict(self)


@dataclass
class Input(FormPiece):
    type: str = 'text'
    placeholder: str = None


@dataclass
class TextArea(FormPiece):
    pass


@dataclass
class Select(FormPiece):
    options: dict = field(default_factory=dict)


@dataclass
class CheckBox(FormPiece):
    options: dict = field(default_factory=dict)
