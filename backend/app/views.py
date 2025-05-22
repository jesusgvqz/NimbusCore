# IMPORTS
## DJANGO
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

## FORMS
from backend.app.forms import LoginForm
from backend.app.forms import ServerForm
from backend.app.forms import ServiceForm

## CIPHERS
from backend.app.hashes import *

## MODELS
from backend.app.models import *


# VIEWS

## LOGIN
def login_view(request):
    loginform = LoginForm()
    return render(request, "login.html", {"form": loginform})

##DASHBOARD
def dashboard_view(request):
    return render(request, 'dashboard.html')
