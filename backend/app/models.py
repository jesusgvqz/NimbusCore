from django.db import models
from datetime import timedelta
from django.utils.timezone import now


# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=128)
    salt=models.CharField(max_length=64, blank=True)

class ContadorIntentos(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    contador = models.PositiveIntegerField()
    ultimo_intento = models.DateTimeField()

    def __str__(self):
        return f"{self.ip} - {self.contador} intentos"

#OTP 
class OTPTemp(models.Model):
    username = models.CharField(max_length=50)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    
    def is_valid(self):
        return (not self.used) and (now() - self.created_at) < timedelta(minutes=3)

