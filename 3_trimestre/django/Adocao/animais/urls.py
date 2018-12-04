from django.urls import path

# importa tudo que tem no views.py do app "animais"
from .views import *
# . indica para o python buscar o views dentro deste diretório
# * indica para importar tudo de lá

urlpatterns = [
    #   ( endereço, método da view, nome da url )
    path('', Index.as_view(), name="index" ),
    path('ajuda/', Ajuda.as_view(), name="ajuda"),
    path('contato/', Contato.as_view(), name="contato"),
    path('sobre/', Sobre.as_view(), name="sobre"),

    path('nova/cidade/', CidadeCreate.as_view(), name='inserir-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidades/', CidadeList.as_view(), name="listar-cidade"),

    path('nova/pessoa/', PessoaCreate.as_view(), name='inserir-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('listar/pessoas/', PessoaList.as_view(), name="listar-pessoa"),

    path('nova/animal/', AnimalCreate.as_view(), name='inserir-animal'),
    path('editar/animal/<int:pk>/', AnimalUpdate.as_view(), name='editar-animal'),
    path('excluir/animal/<int:pk>/', AnimalDelete.as_view(), name='excluir-animal'),
    path('listar/animal/', AnimalList.as_view(), name="listar-animal"),

    path('nova/tipo/', TipoCreate.as_view(), name='inserir-tipo'),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name='editar-tipo'),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name='excluir-tipo'),
    path('listar/tipo/', TipoList.as_view(), name="listar-tipo"),
]
