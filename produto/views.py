from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models


class listaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'


class detalheProduto(View):
    pass


class adicionarAoCarrinho(View):
    pass


class removerDoCarrinho(View):
    pass


class carrinho(View):
    pass


class finalizar(View):
    pass
