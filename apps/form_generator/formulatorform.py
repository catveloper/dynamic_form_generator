# TODO: 각 serializer에 따른 폼을 생성 가능하도록
# TODO: serializer의 필드들에 대응되는 디폴트 필드 정의
# TODO: @데코레이터를 활용해서 formulate에서 사용가능한 항목들 캐싱
# TODO: 폼 제네레이터를 하나의 패키지화 시켜서 어디서든 적용가능하도록
# TODO: url커스텀이 가능하도록
import dataclasses
from typing import List

from rest_framework.serializers import Serializer

formulates: List = []


def get_all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in get_all_subclasses(c)])


@dataclasses
class FormulatorForm:
    name: str
    form_url: str
    summit_url: str
    serializer: Serializer


class FormFactory:
    formulates: List[FormulatorForm] = []

    @staticmethod
    def get_form(cls, name: str):
        return [formulate for formulate in cls.formulates if formulate.name == name][0]



