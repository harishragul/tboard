from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
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