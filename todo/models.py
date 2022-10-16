from django.contrib.auth.models import User
from django.db import models

from core.settings import AUTH_USER_MODEL


class TaskCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'task categories'

    def __str__(self):
        return f'{self.name}'


class GenericTask(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)
    categories = models.ManyToManyField(to=TaskCategory, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserTask(GenericTask):
    user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'UserTask {self.id}'


class GroupTask(GenericTask):
    users = models.ManyToManyField(
        to=AUTH_USER_MODEL
    )

    def __str__(self):
        return f'GroupTask {self.id}'
