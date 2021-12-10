from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    category = models.CharField(max_length=30, choices=[('image', '이미지'), ('audio', '음성'), ('video', '비디오'), ('point_cloud', '포인트 클라우드')])


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