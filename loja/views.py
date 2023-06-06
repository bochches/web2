from django.shortcuts import render
from rest_framework import generics
from .serializers import TamanhoSerializers, CorSerializers, CategoriaSerializers, FornecedorSerializers, ClienteSerializers, LojaSerializers, PagamentoSerializers
from .models import Cor, Tamanho, Categoria, Fornecedor, Cliente, Loja, Pagamento

class CorListAPIView(generics.ListAPIView):
    queryset = Cor.objects.all()
    serializer_class = CorSerializers

class TamanhoListAPI2(generics.ListAPIView):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializers

class CategoriaListAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class FornecedorListAPIView(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializers

class ClienteListAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class LojaListAPIView(generics.ListCreateAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializers

class PagamentoListAPIView(generics.ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializers
