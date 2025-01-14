from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.pagar.as_view(), name="pagar"),
    path('fecharPedido/', views.fecharPedido.as_view(), name="fecharPedido"),
    path('detalhe/', views.detalhe.as_view(), name="detalhe")
]
