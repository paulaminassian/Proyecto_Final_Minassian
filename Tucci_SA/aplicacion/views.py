from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")

def clientes(request):
    contexto = {'clientes': Clientes.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def maritimas(request):
    return render(request, "aplicacion/maritimas.html")

def rutas(request):
    return render(request, "aplicacion/rutas.html")

def precios(request):
    return render(request, "aplicacion/precios.html")