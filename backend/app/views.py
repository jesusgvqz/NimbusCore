# IMPORTS
## GENERAL
import requests
from datetime import timezone
## DJANGO
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.timezone import now

## FORMS
from .forms import LoginForm
from .forms import ServerForm
from .forms import ServiceForm
from .forms import OTPForm

## CIPHERS
from .hashes import password_auth, base64_to_binary

## MODELS
from .models import ContadorIntentos
from .models import OTPTemp

# FUNCTIONS

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

def ip_registrada(ip):
    return ContadorIntentos.objects.filter(pk=ip).exists()

def fecha_en_ventana(fecha, segundos_ventana=settings.SEGUNDOS_INTENTO):
    return (now() - fecha).total_seconds() <= segundos_ventana

def tienes_intentos_login(request):
    ip = get_client_ip(request)

    if not ip_registrada(ip):
        ContadorIntentos.objects.create(ip=ip, contador=1, ultimo_intento=now())
        return True

    registro = ContadorIntentos.objects.get(pk=ip)
    if not fecha_en_ventana(registro.ultimo_intento):
        registro.contador = 1
        registro.ultimo_intento = now()
        registro.save()
        return True

    if registro.contador < settings.NUMERO_INTENTOS:
        registro.contador += 1
        registro.ultimo_intento = now()
        registro.save()
        return True

    registro.ultimo_intento = now()
    registro.save()
    return False

# VIEWS

## LOGIN
def login_view(request):
    template = 'login.html'

    if request.method == 'POST':
        if not tienes_intentos_login(request):
            errores = [f'Debes esperar {settings.SEGUNDOS_INTENTO} segundos antes de volver a intentar']
            return render(request, template, {'errores': errores})

        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = loginform.user
            request.session['otp_user'] = user.username
            return redirect('/otp')


    else:
        loginform = LoginForm()

    return render(request, template, {"form": loginform})

## LOGOUT
def logout_view(request):
    request.session['loggeado'] = False
    request.session.flush()
    return redirect('/login')

##  OTP 
def otp_view(request):
    template = 'otp.html'

    if request.method == 'POST':
        otpform = OTPForm(request.POST)
        if otpform.is_valid():
            otp_ingresado = otpform.cleaned_data['otp']
            username = request.session.get('otp_user')
            if not username:
                return redirect('/login')

            try:
                otp_obj = OTPTemp.objects.get(username=username, otp=otp_ingresado, used=False)
                if otp_obj.is_valid():
                    otp_obj.used = True
                    otp_obj.save()
                    request.session['loggeado'] = True
                    request.session['usuario'] = username
                    return redirect('/dashboard')
            except OTPTemp.DoesNotExist:
                pass

            otpform.add_error(None, 'Código OTP inválido o expirado')
    else:
        otpform = OTPForm()

    return render(request, template, {'form': otpform})

## DASHBOARD
def dashboard_view(request):
    if not request.session.get('loggeado'):
        return redirect('/login')
    return render(request, 'dashboard.html')

