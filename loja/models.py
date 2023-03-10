from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=120)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    CPF = models.CharField(max_length=30)
    CEP = models.CharField(max_length=11)

class Loja(models.Model):
    nome=models.CharField(max_length=120)
    endereco= models.CharField(max_length=120)
    cnpj= models.CharField(max_length=120)
    cidade= models.CharField(max_length=120)
    estado= models.CharField(max_length=2)
    cep= models.CharField(max_length=11)
    email= models.EmailField(max_length=100)
    telefone= models.CharField(max_length=120)

class Pagamento(models.Model):
    nome=models.CharField(max_length=120)