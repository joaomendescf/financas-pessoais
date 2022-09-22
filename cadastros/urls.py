from django.urls import path

from .views import DespesaCartaoCreate, CartaoDeCreditoCreate, FornecedorCreate, CategoriaReceitaCreate, CategoriaDespesaCreate, DespesaCreate, ReceitaCreate, FormaPagamentoCreate
from .views import DespesaCartaoUpdate, CartaoDeCreditoUpdate, FornecedorUpdate, CategoriaReceitaUpdate, CategoriaDespesaUpdate, DespesaUpdate, ReceitaUpdate, FormaPagamentoUpdate
from .views import DespesaCartaoDelete, CartaoDeCreditoDelete, FornecedorDelete, CategoriaReceitaDelete, CategoriaDespesaDelete, DespesaDelete, ReceitaDelete, FormaPagamentoDelete
from .views import CartaoDeCreditoList, FornecedorList, CategoriaDespesaList, CategoriaReceitaList, DespesaList, ReceitaList, FormaPagamentoList

urlpatterns = [
    
    path('cadastrar/fornecedor', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/forma-de-pagamento', FormaPagamentoCreate.as_view(), name='cadastrar-forma-de-pagamento'),
    path('cadastrar/receita', ReceitaCreate.as_view(), name='cadastrar-receita'),
    path('cadastrar/despesa', DespesaCreate.as_view(), name='cadastrar-despesa'),
    path('cadastrar/cartao-de-credito', CartaoDeCreditoCreate.as_view(), name='cadastrar-cartao-de-credito'),
    # path('cadastrar/despesa-cartao', DespesaCartaoCreate.as_view(), name='cadastrar-despesa-cartao'),
    path('cadastrar/despesa-cartao', DespesaCartaoCreate, name='despesa-cartao'),
    path('cadastrar/categoria-receita', CategoriaReceitaCreate.as_view(), name='cadastrar-categoria-receita'),
    path('cadastrar/categoria-despesa', CategoriaDespesaCreate.as_view(), name='cadastrar-categoria-despesa'),
    
    path('editar/fornecedor/<int:pk>', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/forma-de-pagamento/<int:pk>', FormaPagamentoUpdate.as_view(), name='editar-forma-de-pagamento'),
    path('editar/receita/<int:pk>', ReceitaUpdate.as_view(), name='editar-receita'),
    path('editar/despesa/<int:pk>', DespesaUpdate.as_view(), name='editar-despesa'),
    path('editar/cartao-de-credito/<int:pk>', CartaoDeCreditoUpdate.as_view(), name='editar-cartao-de-credito'),
    path('editar/despesa-cartao/<int:pk>', DespesaCartaoUpdate.as_view(), name='editar-despesa-cartao'),
    path('editar/categoria-receita/<int:pk>', CategoriaReceitaUpdate.as_view(), name='editar-categoria-receita'),
    path('editar/categoria-despesa/<int:pk>', CategoriaDespesaUpdate.as_view(), name='editar-categoria-despesa'),
    
    path('excluir/fornecedor/<int:pk>', FornecedorDelete.as_view(), name='excluir-fornecedor'),
    path('excluir/forma-de-pagamento/<int:pk>', FormaPagamentoDelete.as_view(), name='excluir-forma-de-pagamento'),
    path('excluir/receita/<int:pk>', ReceitaDelete.as_view(), name='excluir-receita'),
    path('excluir/despesa/<int:pk>', DespesaDelete.as_view(), name='excluir-despesa'),
    path('excluir/cartao-de-credito/<int:pk>', CartaoDeCreditoDelete.as_view(), name='excluir-cartao-de-credito'),
    path('excluir/despesa-cartao/<int:pk>', DespesaCartaoDelete.as_view(), name='excluir-despesa-cartao'),
    path('excluir/categoria-receita/<int:pk>', CategoriaReceitaDelete.as_view(), name='excluir-categoria-receita'),
    path('excluir/categoria-despesa/<int:pk>', CategoriaDespesaDelete.as_view(), name='excluir-categoria-despesa'),

    path('listar/fornecedor', FornecedorList.as_view(), name='listar-fornecedor'),
    path('listar/forma-de-pagamento', FormaPagamentoList.as_view(), name='listar-forma-de-pagamento'),
    path('listar/receita', ReceitaList.as_view(), name='listar-receita'),
    path('listar/despesa', DespesaList.as_view(), name='listar-despesa'),
    path('listar/cartao-de-credito', CartaoDeCreditoList.as_view(), name='listar-cartao-de-credito'),    
    path('listar/categoria-receita', CategoriaReceitaList.as_view(), name='listar-categoria-receita'),
    path('listar/categoria-despesa', CategoriaDespesaList.as_view(), name='listar-categoria-despesa'),
    
]