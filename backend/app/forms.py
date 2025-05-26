# IMPORTS
## DJANGO
from django import forms

## RECAPTCHA
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

## MODELS
from .models import Usuario

## CIPHERS
from .hashes import password_auth, base64_to_binary

# FORMS
## LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean(self):
        cleaned_data = super().clean()
        cleaned_username = cleaned_data.get('username')
        cleaned_password = cleaned_data.get('password')

        if not cleaned_username or not cleaned_password:
            raise forms.ValidationError('Usuario y contraseña son obligatorios.')
        
        try:
            user = Usuario.objects.get(username=cleaned_username)
        except Usuario.DoesNotExist:
            raise forms.ValidationError('Usuario o contraseña incorrectos.')
        
        salt = base64_to_binary(user.salt)
        if not password_auth(cleaned_password, user.password, salt):
            raise forms.ValidationError('Usuario o contraseña incorrectos.')

        self.user = user
        return cleaned_data
    

## SERVER
class ServerForm(forms.Form):
    servername = forms.CharField(label='Servidor')

## SERVICE
class ServiceForm(forms.Form):
    servicename = forms.CharField(label='Service')

