from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Workspace(models.Model):
    code = models.CharField(_('코드'), max_length=40, unique=True, editable=False)
    name = models.CharField(_('이름'), max_length=50, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='workspaces_owned',
        on_delete=models.PROTECT, verbose_name=_('소유자')
    )
    is_active = models.BooleanField(_('활성'), default=False)

    class Meta:
        verbose_name = _('워크스페이스')
        verbose_name_plural = _('워크스페이스')

    def __str__(self):
        return self.name


class Project(models.Model):

    workspace = models.ForeignKey(
        'Workspace', related_name='projects',
        on_delete=models.PROTECT, verbose_name=_('워크스페이스')
    )
    title = models.CharField(_('제목'), max_length=200)
    category = models.CharField(
        _('카테고리'), max_length=50,
        choices=[
            ('image_annotation', _('이미지 어노테이션')),
            ('video_annotation', _('비디오 어노테이션')),
            ('pcd_annotation', _('PCD 어노테이션'))
        ]
    )

    class Meta:
        verbose_name = _('프로젝트')
        verbose_name_plural = _('프로젝트')

    def __str__(self):
        return self.title


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
