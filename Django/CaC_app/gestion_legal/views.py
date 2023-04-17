from django.shortcuts import render
from django.http import HttpResponse    



def index(request):
    return HttpResponse("Bienvenido al sistema de gestion legal")

def alta_cliente(request):
    return HttpResponse("Alta de clientes")

def baja_cliente(request):
    return HttpResponse("Baja de clientes")

def login(request):
    return HttpResponse("Pagina de login")

def alta_usuario(request):
    return HttpResponse("Alta de usuarios")

def baja_usuario(request):
    return HttpResponse("Baja de usuarios")