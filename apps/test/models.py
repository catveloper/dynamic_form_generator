from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()


class Task(models.Model):
    project = models.ForeignKey(
        'Project', related_name='tasks',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)


class Annotation(models.Model):
    task = models.ForeignKey(
        'Task', related_name='annotations',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='annotations',
        on_delete=models.CASCADE
    )

    data = models.JSONField(default=dict, blank=True)