from django.shortcuts import render
from .models import Cliente
# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html", {"clientes":clientes})

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar(request):
    return render(request, "rel_cliente.html")