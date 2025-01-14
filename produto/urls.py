from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.listaProdutos.as_view(), name="lista"),
    path('<slug>', views.detalheProduto.as_view(), name="detalhe"),
    path('adicionaraocarrinho/', views.adicionarAoCarrinho.as_view(),
         name="adicionaraocarrinho"),
    path('removerdocarrinho/', views.removerDoCarrinho.as_view(),
         name="removerdocarrinho"),
    path('carrinho/', views.carrinho.as_view(), name="carrinho"),
    path('finalizar/', views.finalizar.as_view(), name="finalizar")
]
