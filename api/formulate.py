import apps
from api.serializers import UserSerializer, TaskSerializer, ProjectSerializer, AnnotationSerializer
from apps.form_generator.enums import Widget
from apps.form_generator.formulator import Formulator


# 사실상 viewset을 만들어낼 메타클래스
# 기본적으로 시리얼라이저는 필수 값 ,

class ProjectForm(Formulator):

    name = Widget.TEXT_AREA()
    url = Widget.SELECT()

    class Meta:
        alias = 'project'
        serializer = ProjectSerializer


class AnnotationForm(Formulator):

    data = Widget.TEXT_AREA()

    class Meta:
        alias = 'annotation'
        serializer = AnnotationSerializer


class TaskForm(Formulator):

    name = Widget.SELECT()
    age = Widget.INPUT(help='안녕하세요')
    project = ProjectForm()
    annotations = AnnotationForm()

    class Meta:
        alias = 'task'
        serializer = TaskSerializer


