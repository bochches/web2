from django.contrib import admin

from .models import Fornecedor, Categoria, Cliente, Loja, Pagamento, Cor, Tamanho, Produto, Pedido, Estoque, Carrinho

admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Loja)
admin.site.register(Pagamento)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Estoque)
admin.site.register(Carrinho)