from django.shortcuts import render
from rest_framework import generics
from .serializers import TamanhoSerializers, CorSerializers, CategoriaSerializers, FornecedorSerializers, ClienteSerializers,\
    LojaSerializers, PagamentoSerializers, ProdutoSerialisers, PedidoSerializers, EstoqueSerializers, CarrinhoSerializers
from .models import Cor, Tamanho, Categoria, Fornecedor, Cliente, Loja, Pagamento, Produto, Pedido, Estoque, Carrinho

class CorListAPIView(generics.ListAPIView):
    queryset = Cor.objects.all()
    serializer_class = CorSerializers

class TamanhoListAPI2(generics.ListAPIView):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializers

class CategoriaListAPIView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class FornecedorListAPIView(generics.ListAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializers

class ClienteListAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class LojaListAPIView(generics.ListAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializers

class PagamentoListAPIView(generics.ListAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializers

class ProdutoListAPIView(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerialisers

class PedidoListAPIView(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers

class EstoqueListAPIView(generics.ListAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializers

class CarrinhoListAPIView(generics.ListAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializers