from django.db import models
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    CPF = models.CharField(max_length=30)
    CEP = models.CharField(max_length=11)

    def __str__(self):
        return self.nome, self.endereco, self.cidade, self.estado, self.telefone, self.email, self.CPF, self.CEP

class Loja(models.Model):
    nome=models.CharField(max_length=120)
    endereco= models.CharField(max_length=120)
    cnpj= models.CharField(max_length=120)
    cidade= models.CharField(max_length=120)
    estado= models.CharField(max_length=2)
    cep= models.CharField(max_length=11)
    email= models.EmailField(max_length=100)
    telefone= models.CharField(max_length=120)

    def __str__(self):
        return self.nome, self.endereco, self.cidade, self.estado, self.telefone, self.email, self.cep, self.cnpj

class Pagamento(models.Model):
    nome=models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome=models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    descricao= models.CharField(max_length=120)
    def __str__(self):
        return self.descricao

class Produto(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagem')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=120)
    valor = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=11)
    def image_capa(self):
        return mark_safe('<img src="{}" with="100" />'.format(self.imagem.url))
    image_capa.short_description = 'Capa'
    image_capa.allow_tags = True

class Pedido(models.Model):
    data= models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=11)

class Estoque(models.Model):
    quantidade= models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=11)
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE)

class Carrinho(models.Model):
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagamento= models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    quantidade = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=11)