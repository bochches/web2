from django.contrib import admin

from .models import Fornecedor, Categoria, Cliente, Loja, Pagamento, Cor

admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Loja)
admin.site.register(Pagamento)
admin.site.register(Cor)