# IMPORTS
## DJANGO
from django import forms

## RECAPTCHA
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

# FORMS
## LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

## SERVER
class ServerForm(forms.Form):
    servername = forms.CharField(label='Servidor')

## SERVICE
class ServiceForm(forms.Form):
    servicename = forms.CharField(label='Service')

