from django.db import models

# Create your models here.
#/mysite/core/models.py

from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Livraria(models.Model):
    Titulo = models.CharField(max_length=105)
    Nome_do_autor = models.CharField(max_length=70)
    Assunto = models.CharField(max_length=50)
    Editora = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    Publicacao = models.DateField()


    def __str__(self):
        return self.Titulo

class Despesa(models.Model):
    data_criacao = models.CharField(max_length=35)
    tipo_despesa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)
    forma_pagamento = models.CharField(max_length=40)
    vencimento = models.DateField()
    quitado = models.BooleanField()


    def __str__(self):
        return self.data_criacao

class Compras(models.Model):
    nome = models.CharField(max_length=80)
    descricaoProduto = models.CharField(max_length=95)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMaximo = models.FloatField()

    def __str__(self):
        return self.nome

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartoss = models.IntegerField()
    proprietario = models.CharField(max_length=80)
    valorCondominio = models.FloatField()

    def __str__(self):
        return self.numero

class Anuncio(models.Model):
    cliente = models.CharField(max_length=90)
    textoTitulo = models.CharField(max_length=80)
    preco = models.IntegerField()
    textoAnuncio = models.CharField(max_length=150)
    nomeContato = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    secao = models.CharField(max_length=25)
    tipoAnuncio = models.CharField(max_length=35)

    def __str__(self):
        return self.cliente



