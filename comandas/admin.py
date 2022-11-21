from django.contrib import admin
from .models import Comanda, PedidoComanda, ComentarioComanda


admin.site.register(Comanda)
admin.site.register(PedidoComanda)
admin.site.register(ComentarioComanda)
