from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_clientes, name="customers"),
    path("exibir/<cliente_id>/", views.delete_cliente, name="delete_cliente"),
    path("editar/<cliente_id>/", views.edit_cliente, name="edit_cliente"),
    path("adicionar/", views.adicionar_cliente, name="adicionar_cliente"),
]
