from enum import Enum
from typing import Type

from django.urls import resolve
from rest_framework.reverse import reverse

from apps.form_generator.autoform import *


class Form(Enum):
    INPUT = ('text', Input)
    TEXT_AREA = ('textarea', TextArea)
    SELECT = ('select', Select)
    CHECK_BOX = ('check_box', CheckBox)

    def __init__(self, type: str, form_class: Type[FormUnit]):
        self.type = type
        self.form_class = form_class
