from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)
    distrito =models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img/clientes')
    fecharegistro=models.DateTimeField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    raza = models.CharField(max_length=50)
    años = models.IntegerField()
    sexo = (('M','Macho'),('H','Hembra'))
    alergia =models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img/mascota')
    fecharegistro=models.DateTimeField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Paseador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)
    experiencia = models.CharField(max_length=15)
    edad = models.CharField(max_length=15)
    distrito =models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img/paseador')
    fecharegistro=models.DateTimeField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


