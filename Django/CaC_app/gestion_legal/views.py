from django.shortcuts import render
from django.http import HttpResponse    
from .forms import Alta_cliente_form



def index(request):
    context = []
    return render(request, "gestion_legal/index.html" )

def alta_cliente(request):
    if request.method == "POST":

        alta_cliente_form_view = Alta_cliente_form(request.POST)#completo la instancia del formulario con lo que recibo del request post
   
    else:

        alta_cliente_form_view = Alta_cliente_form()# GET envio al cliente un formulario vacio

    context = {'form': alta_cliente_form_view}
    
    return render(request, "gestion_legal/alta_cliente.html", context)

def baja_cliente(request):
    context = []
    return render(request, "gestion_legal/baja_cliente.html")

def login(request):
    context = []
    return render(request, "gestion_legal/login.html")

def alta_usuario(request):
    context = []
    return render(request, "gestion_legal/alta_usuario.html")

def baja_usuario(request):
    context = []
    return render(request, "gestion_legal/baja_usuario.html")

def servicios(request):
    context = []
    return render(request, "gestion_legal/servicios.html")