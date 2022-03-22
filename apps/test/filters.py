import django_filters
from django_filters import filters

from apps.test.models import Project


class ProjectFilter(django_filters.FilterSet):

    class Meta:
        model = Project
        fields = ['title', 'category']