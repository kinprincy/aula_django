from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html", {"clientes":clientes})

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    if vnome:
        Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail)
    return redirect(fcliente)
