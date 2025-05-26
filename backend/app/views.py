# IMPORTS
## DJANGO
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.views.decorators.csrf import csrf_protect
a
## FORMS
from .forms import LoginForm
from .forms import ServerForm
from .forms import ServiceForm

## CIPHERS
from .hashes import password_auth, base64_to_binary

## MODELS
# from .models import *


# VIEWS

## LOGIN
def login_view(request):
    template = 'login.html'
    
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = loginform.user
            request.session['loggeado'] = True
            request.session['usuario'] = user.username
            return redirect('/dashboard')
    else:
        loginform = LoginForm()

    return render(request, template, {"form": loginform})

## DASHBOARD
def dashboard_view(request):
    return render(request, 'dashboard.html')
