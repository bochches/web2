from rest_framework import serializers
from .models import Cor, Tamanho, Categoria, Fornecedor, Cliente, Loja, Pagamento, Produto, Pedido, Estoque, Carrinho
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

class ProdutoSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('cor', 'fornecedor', 'imagem', 'categoria', 'tamanho', 'descricao', 'valor',)

class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('data',)

class EstoqueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = ('quantidade', 'produto',)

class CarrinhoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ('produto', 'cliente', 'pagamento', 'quantidade',)