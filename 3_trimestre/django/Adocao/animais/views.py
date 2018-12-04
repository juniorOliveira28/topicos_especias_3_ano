# Uma classe simples para exibir uma página simples
from django.views.generic import TemplateView
# Serve para páginas que só tem HTML e talvez alguma consulta
# para listar coisas do banco

from .models import *

#  importar views para inserir alterar ecluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importar a view para listar classes
from django.views.generic.list import ListView

# importar a função para gerar endereços das urls inteiras
from django.urls import reverse_lazy

# Página inicial
class Index(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "pagina_inicial.html" # deve estar na pasta templates


# Página de ajuda
class Ajuda(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "ajuda.html" # deve estar na pasta templates


class Contato(TemplateView):
    template_name = 'contato.html'


class Sobre(TemplateView):
    template_name = 'sobre.html'


class CidadeCreate(CreateView):
    # identificar o modelo
    model = Cidade
    #  define para onde vai redirecionar depois de inserir
    success_url = reverse_lazy('listar-cidade')
    # define qual o templae será usado
    template_name = 'form.html'
    #  define quais campos vão estar no formulário
    fields = ['nome', 'estado']


class CidadeUpdate(UpdateView):
    # identificar o modelo
    model = Cidade
    #  define para onde vai redirecionar depois de inserir
    success_url = reverse_lazy('listar-cidade')
    # define qual o templae será usado
    template_name = 'form.html'
    #  define quais campos vão estar no formulário
    fields = ['nome', 'estado']


class CidadeDelete(DeleteView):
    model = Cidade
    success_url = reverse_lazy('listar-cidade')
    template_name = 'form_delete.html'


class CidadeList(ListView):
    model = Cidade
    template_name = 'cidade_list.html'


class PessoaCreate(CreateView):
    model = Pessoa
    success_url = reverse_lazy("listar-pessoa")
    template_name = 'form.html'
    fields = ['nome', 'emails', 'nascimento', 'cidade']


class PessoaUpdate(UpdateView):
    model = Pessoa
    success_url = reverse_lazy('listar-pessoa')
    template_name = 'form.html'
    fields = ['nome', 'emails', 'nascimento', 'cidade']


class PessoaDelete(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('listar-pessoa')
    template_name = 'form_delete.html'



class PessoaList(ListView):
    model = Pessoa
    template_name = 'pessoa_list.html'

class AnimalCreate(CreateView):
    model = Animal
    success_url = reverse_lazy('listar-animal')
    template_name = 'form.html'
    fields = ['nome', 'raca', 'idade', 'porte', 'tipo']


class AnimalUpdate(UpdateView):
    model = Animal
    success_url = reverse_lazy('listar-animal')
    template_name = 'form.html'
    fields = ['nome', 'raca', 'idade', 'porte', 'tipo']


class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('listar-animal')
    template_name = 'form_delete.html'


class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'

class TipoCreate(CreateView):
    model = Tipo
    success_url = reverse_lazy('listar-tipo')
    template_name = 'form.html'
    fields = ['nome']


class TipoUpdate(UpdateView):
    model = Tipo
    success_url = reverse_lazy('listar-tipo')
    template_name = 'form.html'
    fields = ['nome']


class TipoDelete(DeleteView):
    model = Tipo
    success_url = reverse_lazy('listar-tipo')
    template_name = 'form_delete.html'


class TipoList(ListView):
    model = Tipo
    template_name = 'tipo_list.html'



























    #
