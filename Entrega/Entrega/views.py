from datetime import datetime
from django.http import HttpResponse
from django.template import Context,Template, loader

def bienvenido(request):
    return HttpResponse('bienvenido a mi pagina web')
    
def segunda(request):
    return HttpResponse("""
    <h1> hola </h1>

    <br>
    <br> 
    <p> como estas? </p>
    """)

def diaHoy(request):
    dia = datetime.now()
    documentotexto = f"hoy es: <br> {dia}"
    return HttpResponse(documentotexto)

def nombre(request, nombres):
    docutxt = f"<h1> my name is: </h1> <br><br> {nombres}"
    return HttpResponse(docutxt)

def templa(request, nombre, apellido):
    
    plantilla = loader.get_template("template.html")
    documento = plantilla.render({"nombre":nombre, "apellido":apellido})
    return HttpResponse(documento)
