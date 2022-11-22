from django.shortcuts import render
from .models import familia
from django.template import Template, loader
from django.http import HttpResponse

def familiares(request):

    familiar1=familia(nombre='Angel', apellido='Tang', fecha_nacimiento='1992-2-16', parentesco='Hijo', ocupacion='Administrador de datos', genero='Masculino', edad=30 )
    familiar2=familia(nombre='Julio', apellido='Gonzalez', fecha_nacimiento='1990-11-17', parentesco='Yerno', ocupacion='Administrador de compras', genero='Masculino', edad=32)
    familiar3=familia(nombre='Angela', apellido='Tang', fecha_nacimiento='1994-10-10', parentesco='Hija', ocupacion='Estilista', genero='Femenino', edad=53 )
    familiar4=familia(nombre='Edmar', apellido='Andrade', fecha_nacimiento='1969-09-26', parentesco='Madre', ocupacion='Pastelera', genero='Femenino', edad=28)
    
    toda_familia=[familiar1, familiar2, familiar3, familiar4]

    diccionario={'lista':toda_familia}

    for integrante in toda_familia:
        integrante.save()

    template=loader.get_template('plantilla.html')
    documento=template.render(diccionario)

    return HttpResponse(documento)


