from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.

def familia(request, nombre, apellido, edad, celular, fechanacimiento):
    familia = Familia(nombre= nombre, apellido= apellido, 
    fechanacimiento= fechanacimiento ,edad = edad, celular=celular )
    familia.save()

    return HttpResponse( f"""

    <p> Nombre: {familia.nombre} </p> 
    <p>Apellido: {familia.apellido}</p>
    <p>Fecha de nacimiento: {familia.fechanacimiento}</p>
    <p>Edad: {familia.edad}</p>
    <p>Celular: {familia.celular}</p> 
    """)

def verbbdd(request):
  lista = Familia.objects.all()
  return render(request, "verbbdd.html", {"verbbdd":lista})