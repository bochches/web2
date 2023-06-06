from django.contrib import admin

from .models import Fornecedor, Categoria, Cliente, Loja, Pagamento, Cor, Tamanho, Produto, Pedido, Estoque, Carrinho

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('cor', 'fornecedor', 'imagem', 'categoria', 'tamanho', 'descricao')
    list_display = ['get_cor', 'get_fornecedor', 'image_capa', 'get_categoria', 'get_tamanho', 'descricao']
    readonly_fields = ('get_cor', 'get_fornecedor', 'image_capa', 'get_categoria', 'get_tamanho')

    def get_cor(self, obj):
        return obj.cor.nome
    get_cor.short_description = 'cor'

    def get_fornecedor(self, obj):
        return obj.fornecedor.nome
    get_fornecedor.short_description = 'fornecedor'

    def get_categoria(self, obj):
        return obj.categoria.nome
    get_categoria.short_description = 'categoria'

    def get_tamanho(self, obj):
        return obj.tamanho.descricao
    get_tamanho.short_description = 'tamanho'

admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Loja)
admin.site.register(Pagamento)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido)
admin.site.register(Estoque)
admin.site.register(Carrinho)