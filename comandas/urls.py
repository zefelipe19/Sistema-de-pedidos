from django.urls import path
from .views import Home, ComandaDetalhe, deletar_comada, deletar_pedido

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('comanda/<str:slug>', ComandaDetalhe.as_view(), name='comanda_detalhada'),
    path('deletar-comanda/<str:slug>', deletar_comada, name='deletar_comanda'),
    path('comanda/<str:slug>/deletar-pedido/<int:pk>', deletar_pedido, name='deletar_pedido'),
]
