from django.urls import path
from tasks.views import dashboard, delete_task, update_task

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("delete/task/<int:task_id>", delete_task, name="delete_task"),
    path("update/task/<int:task_id>", update_task, name="update_task"),
]
