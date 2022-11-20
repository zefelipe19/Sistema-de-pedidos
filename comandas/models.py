from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Comanda(models.Model):
    nome = models.CharField(max_length=50)
    data_hora = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    is_visivel = models.BooleanField(default=False)
    is_editavel = models.BooleanField(default=True)

    class Mate:
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'

    def __str__(self):
        return f'{self.nome}'

    def save(self):
        if not self.slug:
            self.slug = slugify(f'posto-praia-cliente-{self.nome}-{self.id}')
        return super().save()

    def get_pedidos(self):
        pedidos = PedidoComanda.objects.filter(comanda__id=self.id)
        return pedidos


class PedidoComanda(models.Model):
    nome = models.CharField(max_length=30)
    data_hora = models.DateTimeField(auto_now_add=True)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)

    class Mate:
        verbose_name = 'Pedido da Comanda'
        verbose_name_plural = 'Pedidos das Comandas'

    def __str__(self):
        return f'{self.nome} ==> {self.comanda}'


class ComentarioComanda(models.Model):
    comentario = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)

    class Mate:
        verbose_name = 'Comentario de Comanda'
        verbose_name_plural = 'Comentarios de Comandas'

    def __str__(self):
        return f'{self.usuario} ==> {self.comanda}'
