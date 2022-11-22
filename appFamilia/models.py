from django.db import models

from django.db import models

class familia(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    parentesco=models.CharField(max_length=40)
    ocupacion=models.CharField(max_length=50)
    genero=models.CharField(max_length=40)
    edad=models.IntegerField()
