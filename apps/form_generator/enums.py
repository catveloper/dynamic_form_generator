from enum import Enum
from typing import Type

from apps.form_generator.components import *


class Form(Enum):
    INPUT = ('text', Input)
    TEXT_AREA = ('textarea', TextArea)
    SELECT = ('select', Select)
    CHECK_BOX = ('check_box', CheckBox)

    def __init__(self, type: str, form_class: Type[FormUnit]):
        self.type = type
        self.form_class = form_class

    def __call__(self, *args, **kwargs):
        return self.form_class(*args, **kwargs)
