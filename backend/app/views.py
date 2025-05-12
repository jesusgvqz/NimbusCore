from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

############################################

def login_view(request):
    form = LoginForm()
    return render(request, "login.html", {"form": form})
