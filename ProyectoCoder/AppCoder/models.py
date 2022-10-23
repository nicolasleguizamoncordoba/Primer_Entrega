from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechanacimiento = models.DateField()
    edad = models.IntegerField()
    celular = models.CharField(max_length=25)

class Mascota(models.Model):
    nombremascota = models.CharField(max_length=100)
    tipomascota = models.CharField(max_length=100)
    edadmascota = models.IntegerField()
    dueñomascota = models.CharField(max_length=100)
