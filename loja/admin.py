from django.contrib import admin

from .models import Fornecedor, Categoria, Cliente

admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Cliente)