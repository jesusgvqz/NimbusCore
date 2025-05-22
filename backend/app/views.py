# IMPORTS
## DJANGO
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

## FORMS
from .forms import LoginForm
from .forms import ServerForm
from .forms import ServiceForm

## CIPHERS
from .hashes import *

## MODELS
from .models import *


# VIEWS

## LOGIN
def login_view(request):
    loginform = LoginForm()
    return render(request, "login.html", {"form": loginform})

## DASHBOARD
def dashboard_view(request):
    return render(request, 'dashboard.html')
