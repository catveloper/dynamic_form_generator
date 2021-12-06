import apps
from api.serializers import UserSerializer, TaskSerializer
from apps.form_generator.enums import Widget
from apps.form_generator.formulator import Formulator


# 사실상 viewset을 만들어낼 메타클래스
# 기본적으로 시리얼라이저는 필수 값 ,
class TestForm(Formulator):

    name = Widget.INPUT()
    age = Widget.INPUT()

    class Meta:
        alias = 'test'
        serializer = TaskSerializer


