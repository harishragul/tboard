from django.contrib import admin
from tasks.models import Task, Status
# Register your models here.

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'organization']
    list_filter = ['organization']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task', 'priority', 'assigned_to', 'assigned_by', 'status', 'due', 'organization']
    search_fields = ['task']
    list_filter = ['status', 'assigned_to', 'assigned_by', 'organization']