from django.contrib import admin

from .models import DespesaCartaoDeCredito, CategoriaDespesa, CategoriaReceita, FormaPagamento, Fornecedor, Despesa, Receita, CartaoDeCredito

# admin.site.register(Caixa)
admin.site.register(CategoriaDespesa)
admin.site.register(FormaPagamento)
admin.site.register(Fornecedor)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(CartaoDeCredito)
admin.site.register(DespesaCartaoDeCredito)
admin.site.register(CategoriaReceita)
