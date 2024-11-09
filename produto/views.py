from django.shortcuts import render, redirect
from .models import Produto
# Create your views here.

def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos":produtos})

def Fcadproduto(request):
    return render(request, "cad_produto.html")

def salvar(request):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    if vnome:
        Produto.objects.create(nome=vnome, descricao=vdescricao, preco=vpreco, quantidade=vquantidade)
    return redirect(fproduto)

def exibir(request, id):
    produto = Produto.objects.get(id=id)

def excluir(request, id):

    produto = Produto.objects.create(id=id)

