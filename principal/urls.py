from  django.urls import path
from .views import findex, fhistoria

urlpatterns = [
    path('', findex), #chama direto pelo servidor
    path('fhistoria/', fhistoria, name='fhistoria'),
    path('findex/', findex, name='findex'), #criar link de

]

