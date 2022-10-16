from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo.models import Task, TaskCategory


class TaskAdmin(ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskCategory)
