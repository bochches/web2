from django.contrib import admin

from .models import Fornecedor, Categoria, Cliente, Loja

admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Loja)