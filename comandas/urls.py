from django.urls import path
from .views import Home, ComandaDetalhe, deletar_comada

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comanda/<str:slug>', ComandaDetalhe.as_view(), name='comanda_datalhada'),
    path('deletar-comanda/<str:slug>', deletar_comada, name='deletar_comanda'),
]
