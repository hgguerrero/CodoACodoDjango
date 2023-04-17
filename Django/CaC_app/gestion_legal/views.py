from django.shortcuts import render
from django.http import HttpResponse    



def index(request):
    context = []
    return render(request, "gestion_legal/index.html" )

def alta_cliente(request):
    return render(request, "gestion_legal/alta_cliente.html")

def baja_cliente(request):
    return render(request, "gestion_legal/baja_cliente.html")

def login(request):
    return render(request, "gestion_legal/login.html")

def alta_usuario(request):
    return render(request, "gestion_legal/alta_usuario.html")

def baja_usuario(request):
    return render(request, "gestion_legal/baja_usuario.html")

def servicios(request):
    return render(request, "gestion_legal/servicios.html")