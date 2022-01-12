from django.conf import settings
from django.db import models


class Project(models.Model):
    class Meta:
        verbose_name = '프로젝트'
    name = models.CharField(max_length=30, verbose_name='이름')
    url = models.URLField()
    category = models.CharField(verbose_name='카테고리', max_length=30, choices=[('image', '이미지'), ('audio', '음성'), ('video', '비디오'), ('point_cloud', '포인트 클라우드')])


class Task(models.Model):
    class Meta:
        verbose_name = '테스크'
    project = models.ForeignKey(
        'Project', related_name='tasks',
        on_delete=models.CASCADE, verbose_name='프로젝트'
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

    long_text = models.TextField(verbose_name='긴문장', help_text='헬프텍스트')

    asd = models.Choices