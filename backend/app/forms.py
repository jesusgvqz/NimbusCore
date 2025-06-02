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

        # OTP - propuesta
        # import requests
        # otp = str(random.randint(100000, 999999))
        # OTPTemp.objects.create(username=user.username, otp=otp)
        # telegramtoken=, chatid=, etc
        # def send_otp_telegram(username, otp):
        #     if not chat_id:
        #         return
        #     mensaje = f"Tu código OTP para NimbusCore es: {otp}"
        #     url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        #     requests.post(url, data={"chat_id": chat_id, "text": mensaje})

        # # Envía por Telegram
        # send_otp_telegram(user.username, otp)

        self.user = user
        return cleaned_data
    
## OTP
class OTPForm(forms.Form):
    otp = forms.CharField(label='Código OTP')

## SERVER
class ServerForm(forms.Form):
    servername = forms.CharField(label='Servidor')

## SERVICE
class ServiceForm(forms.Form):
    servicename = forms.CharField(label='Service')

