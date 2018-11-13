from django.db import models

# Create your models here.

class Cidade(models.Model):
    # nome do atributo = tipoDele (caracteristicas)
    nome = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 2, help_text = "Informe apenas a sigla")

    # imprimir o objeto conforme abaixo
    def __str__(self):
        return self.nome + ' (' + self.estado +')'

class Pessoa(models.Model):
    nome = models.CharField(max_length = 50, help_text = 'Nome Completo')
    emails = models.CharField(max_length = 50)
    nascimento = models.DateField('Data de nascimento')
    # restrict
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    def __str__(self):
        # faz um cast da data para string
        return self.nome + ' - ' + str(self.nascimento)
