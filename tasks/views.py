from django.shortcuts import render, redirect
from tasks.models import Task

# Create your views here.

def main(request):    
    if request.POST:
        task = request.POST.get("task")
        assigned_to = request.POST.get("assigned_to")

        # to store the data into DB
        task_instance = Task(
            task=task,
            assigned_to=assigned_to
        )
        task_instance.save()

        return redirect("task_main")

    # to read data from DB (all data from a table)
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "main.html", context)