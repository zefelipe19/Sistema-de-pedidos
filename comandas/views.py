from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages

# Project imports
from .models import Comanda, PedidoComanda, ComentarioComanda


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            comandas = Comanda.objects.all().filter(usuario=request.user)
            context = {
                'comandas': comandas,
            }
            return render(request, 'index.html', context)
        return render(request, 'index.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        nova_comanda = Comanda(
            nome=nome,
            usuario=request.user)
        messages.success(request, f'Comanda {nova_comanda} criada com sucesso.')
        nova_comanda.save()
        return redirect('home')


class ComandaDetalhe(View):
    def get(self, request, slug):
        comanda = Comanda.objects.get(slug=slug)

        context = {
            'comanda': comanda,
        }
        return render(request, 'comanda.html', context)

    def post(self, request, slug):
        nome_pedido = request.POST.get('nome')
        quantidade_pedido = request.POST.get('quantidade')

        if nome_pedido and quantidade_pedido:
            novo_pedido = PedidoComanda(
                nome=nome_pedido,
                quantidade=quantidade_pedido,
                comanda=Comanda.objects.get(slug=slug),
                quem_fez=request.user,
            )
            messages.success(request, f'Pedido de {nome_pedido} foi adicionado!')
            novo_pedido.save()
            return redirect('comanda_datalhada', slug)
        
        comentario = request.POST.get('comentario')
        if comentario:
            novo_comentario = ComentarioComanda(
                comentario=comentario,
                usuario=request.user,
                comanda=Comanda.objects.get(slug=slug)
            )
            messages.success(request, f'Comentario foi adicionado!')
            novo_comentario.save()
            return redirect('comanda_datalhada', slug)


def deletar_comada(request, slug):
    comanda = Comanda.objects.get(slug=slug)
    messages.error(request, f'A comanda {comanda} foi apagada!')
    comanda.delete()
    return redirect('home')