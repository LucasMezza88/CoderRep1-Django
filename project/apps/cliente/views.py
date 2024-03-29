from django.shortcuts import render

from . import models

def index(request):
    context = {"app_name": "Coderhouse"}
    return render(request, "cliente/index.html", context)

def pais_list(request):
    paises = models.Pais.objects.all()
    return render(request, "cliente/pais_list.html", {"paises": paises})

def cliente_list(request):
    clientes = models.Cliente.objects.all()
    return render(request, "cliente/cliente_list.html", {"clientes": clientes})