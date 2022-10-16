from django.contrib import admin

from todo.models import UserTask, GroupTask, TaskCategory


class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_completed', 'created_at', 'updated_at')


class GroupTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_completed', 'updated_at')


admin.site.register(UserTask, UserTaskAdmin)
admin.site.register(GroupTask, GroupTaskAdmin)
admin.site.register(TaskCategory)
