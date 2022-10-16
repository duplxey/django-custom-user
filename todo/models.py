from django.contrib.auth.models import User
from django.db import models


class TaskCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'task categories'

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)
    categories = models.ManyToManyField(to=TaskCategory, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task ${self.id}'
