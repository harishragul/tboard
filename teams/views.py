from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from teams.forms import OrganizationForm
from teams.models import Organization

# Create your views here.
def register_view(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            context = {
                "error": "username already exist!"
            }
            return render(request, "register.html", context)
        
        User.objects.create_user(username=username, password=password)
        return redirect("login")
        
    return render(request, "register.html")

def login_view(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            context = {
                "error": "Invalid username or password"
            }
            return render(request, "login.html", context)
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def organization_view(request):
    if request.user.is_superuser:
        message = None

        if request.POST:
            try:
                organization_form = OrganizationForm(request.POST)
                if organization_form.is_valid():
                    organization_form.save()
                    return redirect('organization')
                else:
                    message = "Invalid Form Data!"
            except Exception as error:
                message = f"{error}"
        
        organization_form = OrganizationForm()
        organizations = Organization.objects.all()
        
        context = {
            'organizations': organizations,
            'organization_form': organization_form,
            'message': message
        }
        return render(request, 'organization.html', context)
    else:
        return HttpResponse("Access Denied!")