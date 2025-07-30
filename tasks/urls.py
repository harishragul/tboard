from django.urls import path
from tasks.views import main

urlpatterns = [
    path("main/", main, name="task_main"),
]
