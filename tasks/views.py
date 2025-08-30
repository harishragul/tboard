from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from teams.models import Organization, Member
from tasks.forms import TaskForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    member = Member.objects.filter(user__id=request.user.id).first()
    organization = member.organization if member else None

    task_form = TaskForm(organization=organization, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, organization=organization, user=request.user)
        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.organization = organization
            # Set assigned_by to the current user's member record
            if member:
                task_instance.assigned_by = member
            task_instance.save()
            return redirect("dashboard")

    # to read data from DB (all data from a table)
    tasks = Task.objects.filter(organization=organization)

    context = {
        "tasks": tasks,
        "username": request.user.username,
        "task_form": task_form
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='login')
def delete_task(request, task_id):
    # to delete data from DB (for particular primary key)
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("dashboard")

@login_required(login_url='login')
def update_task(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    if request.POST:
        # to update data from DB (for particular primary key)
        task_instance.task = request.POST.get("task") or task_instance.task
        task_instance.assigned_to = request.POST.get("assigned_to") or task_instance.assigned_to
        task_instance.save()
        return redirect("dashboard")
    
    context = {
        'task': task_instance
    }

    return render(request, "update.html", context)

