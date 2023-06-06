from rest_framework import serializers
from .models import Cor, Tamanho, Categoria, Fornecedor, Cliente, Loja, Pagamento
class CorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = ('nome',)

class TamanhoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields = ('descricao',)

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome',)

class FornecedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ('nome', 'endereco', 'cidade', 'estado', 'telefone', 'email',)
class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'cidade', 'estado', 'telefone', 'email', 'CPF', 'CEP',)

class LojaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('nome', 'endereco', 'cidade', 'estado', 'telefone', 'email', 'cep', 'cnpj',)

class PagamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ('nome',)
