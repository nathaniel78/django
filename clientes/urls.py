from django.urls import path
from .views import clientes_listar, clientes_novo, clientes_atualizar, clientes_excluir

urlpatterns = [
    path('listar/', clientes_listar, name='clientes_listar'),
    path('novo/', clientes_novo, name='clientes_novo'),
    path('atualizar/<int:id>', clientes_atualizar, name='clientes_atualizar'),
    path('excluir/<int:id>', clientes_excluir, name='clientes_excluir'),
]