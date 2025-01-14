from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.criar.as_view(), name="criar"),
    path('atualizar/', views.atualizar.as_view(), name="atualizar"),
    path('login/', views.login.as_view(), name="login"),
    path('logout/', views.logout.as_view(), name="logout")
]
