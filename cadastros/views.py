from calendar import month
from .models import DespesaCartaoDeCredito, CategoriaReceita, CartaoDeCredito, CategoriaDespesa, FormaPagamento, Fornecedor, Despesa, Receita
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
import datetime
import paginas.views
from cadastros.forms.form_despesa_cartao import FormDespesaCartaoCredito
from django.shortcuts import render
from django.contrib import messages

#################### FORNECEDOR #######################


class FornecedorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Fornecedor
    fields = ['nome', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')
    login_url = reverse_lazy('login')
    group_required = ["Administrador", "Docente"]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Fornecedor"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FornecedorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ['nome', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')
    login_url = reverse_lazy('login')
    group_required = ["Administrador", "Docente"]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Fornecedor"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FornecedorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedor')
    login_url = reverse_lazy('login')
    group_required = ["Administrador", "Docente"]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Fornecedor"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FornecedorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'cadastros/listas/listar-fornecedor.html'
    login_url = reverse_lazy('login')
    group_required = ["Administrador", "Docente"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


#################### Categoria Despesa #######################

class CategoriaDespesaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = CategoriaDespesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Categoria de Despesa"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaDespesaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = CategoriaDespesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Categoria de Despesa"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaDespesaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CategoriaDespesa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Categoria de Despesa"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaDespesaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = CategoriaDespesa
    template_name = 'cadastros/listas/listar-categoria-despesa.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


#################### CATEGORIA RECEITA #######################

class CategoriaReceitaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = CategoriaReceita
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Categoria de Receita"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaReceitaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = CategoriaReceita
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Categoria de Receita"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaReceitaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CategoriaReceita
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Categoria de Receita"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CategoriaReceitaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = CategoriaReceita
    template_name = 'cadastros/listas/listar-categoria-receita.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


#################### FORMA DE PAGAMENTO #######################
class FormaPagamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = FormaPagamento
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-forma-de-pagamento')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Forma de Pagamento"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FormaPagamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = FormaPagamento
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-forma-de-pagamento')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Forma de Pagamento"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FormaPagamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = FormaPagamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-forma-de-pagamento')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Forma de Pagamento"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class FormaPagamentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = FormaPagamento
    template_name = 'cadastros/listas/listar-forma-de-pagamento.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context

#################### DESPESA #######################


class DespesaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Despesa
    fields = ['dia', 'mes', 'ano', 'categoria', 'fornecedor', 'descricao',
              'forma_de_pagamento', 'parcelamento', 'valor', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Despesa"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)

        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


class DespesaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = ['dia', 'mes', 'ano', 'categoria', 'fornecedor', 'descricao',
              'forma_de_pagamento', 'parcelamento', 'valor', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Despesa"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class DespesaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-despesa')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Despesa"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class DespesaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Despesa
    template_name = 'cadastros/listas/listar-despesa.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context

#################### RECEITA #######################


class ReceitaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Receita
    fields = ['dia', 'mes', 'ano', 'categoria', 'descricao',
              'forma_de_pagamento', 'parcelamento', 'valor', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Receita"
        context['botao'] = "Cadastrar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class ReceitaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Receita
    fields = ['dia', 'mes', 'ano', 'categoria', 'descricao',
              'forma_de_pagamento', 'parcelamento', 'valor', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Receita"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class ReceitaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-receita')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Receita"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class ReceitaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Receita
    template_name = 'cadastros/listas/listar-receita.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context

#################### CARTAO DE CREDITO #######################


class CartaoDeCreditoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = CartaoDeCredito
    fields = ['nome', 'bandeira', 'numero', 'nome_titular',
              'vencimento_pagamento', 'codigo_seguranca', 'data_validade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cartao-de-credito')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Cartão de Crédito"
        context['botao'] = "Cadastrar"
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        return context


class CartaoDeCreditoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = CartaoDeCredito
    fields = ['nome', 'bandeira', 'numero', 'nome_titular',
              'vencimento_pagamento',  'codigo_seguranca', 'data_validade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cartao-de-credito')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Cartão de Crédito"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CartaoDeCreditoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CartaoDeCredito
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cartao-de-credito')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Cartão de Crédito"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class CartaoDeCreditoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = CartaoDeCredito
    template_name = 'cadastros/listas/listar-cartao-de-credito.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context

#################### DESPESA CARTAO DE CREDITO #######################


def DespesaCartaoCreate(request):

    # import datetime

    context = {
        'titulo': "Cadastro de Despesa de Cartão de Crédito",
        'botao': "Cadastrar",
        'cartoes': CartaoDeCredito.objects.filter().order_by('nome'),
        'ano_atual': datetime.date.today().year,
        'mes_atual': paginas.views.converteTexto(datetime.date.today().month),
        'form': FormDespesaCartaoCredito(),
    }

    if request.method == 'POST':
        form = FormDespesaCartaoCredito(request.POST)

        if form.is_valid():
            data = form.cleaned_data['data']
            descricao = form.cleaned_data['descricao']
            fornecedor = form.cleaned_data['fornecedor']
            valor = form.cleaned_data['valor']
            parcelamento = form.cleaned_data['parcelamento']
            cartao = form.cleaned_data['cartao']
            fatura = form.cleaned_data['fatura']
            mes = 1
            if fatura=='Janeiro':
                mes = 1
            elif fatura=='Fevereiro':
                mes = 2
            elif fatura=='Março':
                mes = 3
            elif fatura=='Abril':
                mes = 4
            elif fatura=='Maio':
                mes = 5
            elif fatura=='Junho':
                mes = 6
            elif fatura=='Julho':
                mes = 7
            elif fatura=='Agosto':
                mes = 8
            elif fatura=='Setembro':
                mes = 9
            elif fatura=='Outubro':
                mes = 10
            elif fatura=='Novembro':
                mes = 11
            elif fatura=='Dezembro':
                mes = 12

            parcelamento_int = int(parcelamento)
            valor_parcelado = float(valor)/parcelamento_int

            for i in range(1, parcelamento_int + 1):
                num_texto = str(i)+'/'+parcelamento
                # data = data + datetime.timedelta(days=30)
                mes_texto = paginas.views.converteTexto(mes)
                mes += 1
                DespesaCartaoDeCredito.objects.create(
                    data=data,
                    valor=valor_parcelado,
                    cartao=cartao,
                    parcelamento=num_texto,
                    descricao=descricao,
                    fornecedor=fornecedor,
                    fatura=mes_texto)

            return render(request, 'cadastros/despesa-cartao.html', context)
        else:
            context['form'] = form
            return render(request, 'cadastros/despesa-cartao.html', context)

    return render(request, 'cadastros/despesa-cartao.html', context)

# class DespesaCartaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

#     model = DespesaCartaoDeCredito
#     fields = ['data', 'cartao', 'descricao', 'fornecedor', 'valor', 'parcelamento']
#     # fields = '__all__'
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('cadastrar-despesa-cartao')
#     login_url = reverse_lazy('login')
#     group_required = ['Administrador']

#     def form_valid(self, form):
#         form.instance.usuario = self.request.user
#         url = super().form_valid(form)
#         return url

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['titulo'] = "Cadastro de Despesa de Cartão de Crédito"
#         context['botao'] = "Cadastrar"
#         context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
#         context['ano_atual'] = datetime.date.today().year
#         context['mes_atual'] = paginas.views.converteTexto(datetime.date.today().month)
#         return context


class DespesaCartaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = DespesaCartaoDeCredito
    fields = ['fatura', 'data', 'cartao', 'descricao',
              'fornecedor', 'valor', 'parcelamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-despesa-cartao')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar de Despesa de Cartão de Crédito"
        context['botao'] = "Salvar"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class DespesaCartaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = DespesaCartaoDeCredito
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('cadastrar-despesa-cartao')
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_excluir'] = "Despesa de Cartão de Crédito"
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        return context


class DespesaCartaoDeCreditoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = DespesaCartaoDeCredito
    template_name = 'cartao.html'
    login_url = reverse_lazy('login')
    group_required = ['Administrador']

    def get_context_data(self, **kwargs):

        # from paginas.views import converteTexto

        # data = DespesaCartaoDeCredito.objects.values('data')
        # valores = []
        # for val in data:
        #     mes = converteTexto(val['data'].month)
        #     valores.append(mes)

        # set_valores = set(valores)

        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = paginas.views.converteTexto(
            datetime.date.today().month)
        # context['meses_cartao_credito'] = set_valores
        return context
