from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        user = authenticate(request=request, username=username, password=password)
        login(request=request, user=user)
        return redirect("dashboard")
        
    return render(request, "register.html")

def login_view(request):
    pass

def  logout_view(request):
    pass