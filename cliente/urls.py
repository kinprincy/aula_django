"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import fcliente, Fcadcliente, salvar_cliente, excluir_cliente, exibir_cliente, update_cliente, flogin, ftelacli, logar, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fcliente),
    path('Fcadcliente/', Fcadcliente, name='Fcadcliente'),
    path('salvar_cliente/', salvar_cliente, name='salvar_cliente'),
    path('excluir_cliente/<int:id>', excluir_cliente, name='excluir_cliente'),
    path('exibir_cliente/<int:id>', exibir_cliente, name='exibir_cliente'),
    path('exibir_cliente/', exibir_cliente, name='exibir_cliente'),
    path('update_cliente/<int:id>', update_cliente, name='update_cliente'),
    path('flogin/', flogin, name='flogin'),
    path('ftelacli/', ftelacli, name='ftelacli'),
    path('logar/', logar, name='logar'),
    path('logout/', logout, name='logout'),






]
