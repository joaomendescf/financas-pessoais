from django.views.generic import TemplateView
from cadastros.models import CartaoDeCredito, CategoriaDespesa, CategoriaReceita, Receita, Despesa, FormaPagamento, DespesaCartaoDeCredito

from django.shortcuts import render
from django.http import request
import datetime

############################################## PAGINA INICIAL ##################################
class PaginaInicial(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year 
        context['mes_atual'] = converteTexto(datetime.date.today().month)

        return context

############################################## PENDENCIAS ##################################
class Pendencias(TemplateView):
    template_name = 'pendencias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = converteTexto(datetime.date.today().month)
        context['meses'] = buscarMesesRegistros()
        context['despesa'] = Despesa.objects.all().filter(status='Pendente', mes=context['mes'])
        context['receita'] = Receita.objects.all().filter(status='Pendente', mes=context['mes'])
        
        return context

############################################## PAGINA SOBRE ##################################
class PaginaSobre(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = converteTexto(datetime.date.today().month)
        return context

############################################## PAGINA CARTAO ##################################


class PaginaCartao(TemplateView):
    template_name = 'cartao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # data = DespesaCartaoDeCredito.objects.values('data')
        # valores = []
        # for val in data:
        #     mes = converteTexto(val['data'].month)
        #     valores.append(mes)

        # set_valores = set(valores)

        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        context['meses_cartao_credito'] = meses
        context['cartoes'] = CartaoDeCredito.objects.all().order_by('nome')
        context['cartao'] = DespesaCartaoDeCredito.objects.filter(
            cartao_id=context['id']).filter(fatura=context['mes']).order_by('data')
        context['nome_cartao'] = CartaoDeCredito.objects.get(
            id=context['id']).nome
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = converteTexto(datetime.date.today().month)

        def somarCartao():
            soma = 0.00
            for item in context['cartao']:
                soma += float(item.valor)
            return soma

        context['soma_valor'] = somarCartao()

        return context


############################################## COLETAR ID Categoria D/R #########################
def buscarIdCategoriaRecDes(tipo, categoria):
    if tipo =='despesa':
        dados = CategoriaDespesa.objects.filter(nome=categoria)
    if tipo =='receita':
        dados = CategoriaReceita.objects.filter(nome=categoria)
    return dados[0].id

################################## BUSCAR DADOS DE DESPESAS - FILTROS MES E ANO ####################

def converteTexto(mes):
    if mes == 1:
        mes_selecionado = "Janeiro"
    elif mes == 2:
        mes_selecionado = "Fevereiro"
    elif mes == 3:
        mes_selecionado = "Março"
    elif mes == 4:
        mes_selecionado = "Abril"
    elif mes == 5:
        mes_selecionado = "Maio"
    elif mes == 6:
        mes_selecionado = "Junho"
    elif mes == 7:
        mes_selecionado = "Julho"
    elif mes == 8:
        mes_selecionado = "Agosto"
    elif mes == 9:
        mes_selecionado = "Setembro"
    elif mes == 10:
        mes_selecionado = "Outubro"
    elif mes == 11:
        mes_selecionado = "Novembro"
    elif mes == 12:
        mes_selecionado = "Dezembro"

    return mes_selecionado



################################## BUSCAR DADOS DE DESPESAS - FILTROS MES E ANO ####################
def buscarDadosMes(tipo, mes, idCategoria, contexto):
    
    mes_selecionado = converteTexto(mes)

    if tipo =='despesa':
        dados = Despesa.objects.filter(categoria_id=idCategoria).filter(
        mes=mes_selecionado).filter(ano=contexto)
    elif tipo =='receita':
        dados = Receita.objects.filter(categoria_id=idCategoria).filter(
        mes=mes_selecionado).filter(ano=contexto)
    total = 0.0
    total_mensal = []
    for i in dados:
        total += float(i.valor)
    total_mensal.append(total)
    return total_mensal

############################### CALCULA VALOR DAS DESPESAS E RETIRA OS COLCHETES ####################


def calculaReceitaDespesa(tipo, classe, contexto):
    total = []
    id = buscarIdCategoriaRecDes(tipo, classe)
    
    for i in range(1, 13):
        total.append(buscarDadosMes(tipo, i, id, contexto))
    cont = 0
    for i in total:        
        valor = str(i)[1:-1].replace('0.0', '0,00')
        if valor == '0,00':
            valor = valor.replace('0,00', '-')
        total[cont] = valor        
        cont += 1
   
    return total


############################################## Forma listagem final ################################
def formarDicionarioDados(tipo, tamanhoLista, contexto):
    lista_itens = []
    for i in range(0, tamanhoLista):
        if tipo == 'despesa':
            dict = {CategoriaDespesa.objects.filter()[i]: calculaReceitaDespesa(tipo,
                CategoriaDespesa.objects.filter()[i], contexto)}
        elif tipo == 'receita':
            dict = {CategoriaReceita.objects.filter()[i]: calculaReceitaDespesa(tipo,
                CategoriaReceita.objects.filter()[i], contexto)}            
        lista_itens.append(dict)

    return lista_itens


############################################## BUSCAR DESPESAS DO MES E ANO #######################
def buscarRecDesMes(tipo, mes, contexto):
    total = 0.0
    if tipo == 'receita':
        dados = list(Receita.objects.filter(mes=mes).filter(ano=contexto))
    elif tipo == 'despesa':
        dados = list(Despesa.objects.filter(mes=mes).filter(ano=contexto))

    for i in dados:
        total += float(i.valor)

    total = str(total).replace('0.0', '0,00')
    if total == '0,00':
        total = total.replace('0,00', '-')
    
    return total

############################################## PAGINA RESUMO MENSAL################################

class PaginaResumoMensal(TemplateView):
    template_name = 'resumo-mensal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartoes'] = CartaoDeCredito.objects.filter().order_by('nome')
        context['categoria'] = CategoriaDespesa.objects.filter()
        context['ano_atual'] = datetime.date.today().year
        context['anos'] = buscarAnosRegistros()
        context['mes_atual'] = converteTexto(datetime.date.today().month)

        ####################### Dados tabela Despesa ###############################

        lista_com_valores_categoria_despesa = list(CategoriaDespesa.objects.filter())
        qtd_itens_lista_categoria_despesa = len(lista_com_valores_categoria_despesa)
        lista_itensDes = formarDicionarioDados('despesa',
            qtd_itens_lista_categoria_despesa, context['ano'])
        context['valoresDespesa'] = lista_itensDes

        ####################### Dados tabela Receita ###############################

        lista_com_valores_categoria_receita = list(CategoriaReceita.objects.filter())
        qtd_itens_lista_categoria_receita = len(lista_com_valores_categoria_receita)
        
        lista_itensRec = formarDicionarioDados('receita',
            qtd_itens_lista_categoria_receita, context['ano'])
        context['valoresReceita'] = lista_itensRec     

       ########################## VALOR TOTAL DESPESA ##########################

        lista_mensalDes = []
        for i in range(1, 13):
            mes = converteTexto(i)
            lista_mensalDes.append(buscarRecDesMes(
                'despesa',  mes, context['ano']))
        context['totaisDespesa'] = lista_mensalDes

       ########################## VALOR TOTAL RECEITA ##########################

        lista_mensalRec = []
        for i in range(1,13):
            mes = converteTexto(i)
            lista_mensalRec.append(buscarRecDesMes('receita',  mes, context['ano']))
        context['totaisReceita'] = lista_mensalRec

        return context

################################# BUSCAR ANOS COM REGISTROS R/D ###############################
def buscarAnosRegistros(): 
    anos = Despesa.objects.all()

    lista_anosDespesa = []
    for i in anos:
        lista_anosDespesa.append(i.ano)
    
    anos = Receita.objects.all()
    lista_anosReceita = []
    for i in anos:
        lista_anosReceita.append(i.ano)

    listaAnosFinal = list(lista_anosReceita) + (lista_anosDespesa)
    listaAnos = set(listaAnosFinal)

    return listaAnos

################################# BUSCAR MESES COM REGISTROS R/D ###############################
def buscarMesesRegistros(): 
    meses = Despesa.objects.all()

    lista_mesesDespesa = []
    for i in meses:
        lista_mesesDespesa.append(i.mes)
    
    meses = Receita.objects.all()
    lista_mesesReceita = []
    for i in meses:
        lista_mesesReceita.append(i.mes)

    listaMesesFinal = list(lista_mesesReceita) + (lista_mesesDespesa)
    listaMeses = set(listaMesesFinal)

    return listaMeses


############################################## PAGINA RESUMO ANUAL ##################################
class PaginaResumoAnual(TemplateView):

    template_name = 'resumo-anual.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        despesas = Despesa.objects.filter()
        context['ano_atual'] = datetime.date.today().year
        context['mes_atual'] = converteTexto(datetime.date.today().month)

        receita_mes = []
        total_receitas = 0.0
        for i in range(1,13):
            receita_mensal = 0.0
            mes_texto = converteTexto(i)
            receitas = Receita.objects.filter(mes=mes_texto).filter(ano=context['ano'])
            for rec in receitas:
                receita_mensal += float(rec.valor)
                total_receitas += float(rec.valor)
            receita_mes.append(float(receita_mensal))

        despesa_mes = []
        total_despesas = 0.0
        for i in range(1,13):
            despesa_mensal = 0.0
            mes_texto = converteTexto(i)
            despesas = Despesa.objects.filter(mes=mes_texto).filter(ano=context['ano'])
            for desp in despesas:
                despesa_mensal += float(desp.valor)
                total_despesas += float(desp.valor)
            despesa_mes.append(float(despesa_mensal))
        
        context['valores_mensaisDes'] = despesa_mes
        context['valores_mensaisRec'] = receita_mes

        total = []
        for i in range(0,12):
            total.append(receita_mes[i] - despesa_mes[i])

        context['saldo'] = total
        context['anos'] = buscarAnosRegistros()
        
        return context
