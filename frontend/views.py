from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from frontend.forms import CustomUserCreationForm


@login_required
def home(request):
    return render(request, 'frontend/home.html')

@login_required
def profile(request):
    return render(request, 'frontend/profile.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "frontend/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")