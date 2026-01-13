from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'partials/home.html')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST.get('email')
            user.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "partials/signup.html", {"form": form})


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password."

    return render(request, "partials/login.html", {"error": error})

@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "partials/dashboard.html", {"profile": profile})

def logout_view(request):
    logout(request)
    return redirect("home")