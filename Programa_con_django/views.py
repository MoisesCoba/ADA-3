from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


#creacion de las vistas

def nombre(request):
 return render(request,"agregar_nombre.html")

def buscar(request):

 mensaje="Vienbenido: %r" %request.get["nom"]
     
return HttpResponse(mensaje)

