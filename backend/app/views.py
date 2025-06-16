# IMPORTS
## GENERAL
from math import e
import requests
from datetime import timezone
## DJANGO
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.timezone import now

## FORMS
from .forms import LoginForm
from .forms import ServidorForm
from .forms import ServiceForm
from .forms import OTPForm
from django import forms

## SSH
from .ssh_utils import setup_ssh_key

## PARAMIKO
import paramiko
## CIPHERS
from .hashes import password_auth, base64_to_binary

## MODELS
from .models import ContadorIntentos
from .models import OTPTemp
from .models import Servidor

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


## AddServer
def agregarServidor(request):
    messageSuccess = None
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #Extraer datos del formulario
            nombre=cd['nombre']
            ip=cd['ip']
            puerto=cd['puerto']
            usuario=cd['usuario']
            password = cd['password']
            
            #Probar conexion con paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip, puerto, usuario, password=password ,timeout=30)
                # Si se conecta guarda la BD
                servidor = Servidor(
                    nombre=nombre,
                    ip=ip,
                    puerto=puerto,
                    usuario=usuario
                )
                servidor.save()

                setup_ssh_key(ip, puerto, usuario, password)
                messageSuccess = "Servidor agregado correctamente."
                form = ServidorForm()
                # return redirect('/dashboard')
            except Exception as e:
               # print(f"Error detallado de conexión SSH: {e}")
                form.add_error(None, f"Error al conectar al servidor: {str(e)}")
            finally:
                ssh.close()
    else:
        form = ServidorForm()
            
    return render(request, 'addServ.html', {
    'form': form,
    'messageSuccess': messageSuccess
})

