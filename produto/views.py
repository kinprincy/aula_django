from django.shortcuts import render
from .models import Produto
# Create your views here.

def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "cad_produto.html", {"produtos":produtos})
