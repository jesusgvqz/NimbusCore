from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=128)
    salt=models.CharField(max_length=64, blank=True)