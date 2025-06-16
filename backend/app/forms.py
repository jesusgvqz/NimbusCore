# IMPORTS
import requests
import environ
import random
## DJANGO
from django import forms

## RECAPTCHA
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

## MODELS
from .models import Usuario, OTPTemp, Servidor

## CIPHERS
from .hashes import password_auth, base64_to_binary

# FORMS
## LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu usuario'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu contraseña'
        })
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'mt-3'}))

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
        
        otp = str(random.randint(100000, 999999))
        OTPTemp.objects.create(username=user.username, otp=otp)
        send_otp_telegram(user.username, otp)

        self.user = user
        return cleaned_data



# OTP      
def send_otp_telegram(username, otp):
    CHAT_ID = '-1002568646962'
    TELEGRAM_TOKEN = '7974123495:AAFOPbGrJoEpyIxoZxcIdp_PV4K83oTelT8'
    
    mensaje = f"Hola {username}, tu código OTP para NimbusCore es: {otp}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": mensaje
        }, timeout=3)
    except Exception as e:
        print(f"[ERROR] No se pudo enviar el OTP por Telegram: {e}")

    
## OTP
class OTPForm(forms.Form):
    otp = forms.CharField(
        label='Código OTP',
        max_length=6,
        widget=forms.TextInput(attrs={
            'placeholder': 'Introduce tu código OTP',
            'class': 'form-control'
        })
    )

## SERVER
class ServidorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    class Meta:
        model = Servidor
        fields = ['nombre', 'ip', 'puerto', 'usuario',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.update({'class': 'form-control'})

## SERVICE
class ServiceForm(forms.Form):
    servicename = forms.CharField(label='Service')

