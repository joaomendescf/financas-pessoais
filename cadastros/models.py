from datetime import datetime
from django.db import models

import datetime

from django.contrib.auth.models import User

class Fornecedor(models.Model):

    ESTADOS = {
    ('AC',	'Acre'),
    ('AL',	'Alagoas'),
    ('AP',	'Amapá'),
    ('AM',	'Amazonas'),
    ('BA',	'Bahia'),
    ('CE',	'Ceará'),
    ('DF',	'Distrito Federal'),
    ('ES',	'Espirito Santo'),
    ('GO',	'Goiás'),
    ('MA',	'Maranhão'),
    ('MT',	'Mato Grosso'),
    ('MS',	'Mato Grosso do Sul'),
    ('MG',	'Minas Gerais'),
    ('PA',	'Pará'),
    ('PB',	'Paraíba'),
    ('PR',	'Parana'),
    ('PE',	'Pernambuco'),
    ('PI',	'Piauí'),
    ('RJ',	'Rio de Janeiro'),
    ('RJ',	'Rio de Janeiro'),
    ('RS',	'Rio Grande do Norte'),
    ('RS',	'Rio Grande do Sul'),
    ('RO',	'Rondônia'),
    ('RR',	'Roraima'),
    ('SC',	'Santa Catarina'),
    ('SP',	'São Paulo'),
    ('SE',	'Sergipe'),
    ('TO',	'Tocantins'),
    }

    nome = models.CharField(max_length=50, blank=False)
    cidade = models.CharField(max_length=20, blank=False, default='Ubajara')
    estado = models.CharField(max_length=2, choices=ESTADOS, default='CE')

    def __str__(self):
        return "{} ({}-{})".format(self.nome, self.cidade, self.estado)
     
class CategoriaDespesa(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nome
    
class CategoriaReceita(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nome

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nome

class CartaoDeCredito(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    bandeira = models.CharField(max_length=50, blank=False)
    numero = models.PositiveIntegerField(blank=False)         
    nome_titular = models.CharField(max_length=50, blank=False)
    vencimento_pagamento = models.PositiveIntegerField(blank=False)         
    codigo_seguranca = models.PositiveIntegerField(blank=False)         
    data_validade = models.DateField(blank=False)         
    
    def __str__(self):
        return self.nome

class DespesaCartaoDeCredito(models.Model):

    CHOICE_MESES = {
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    }

    hoje = datetime.datetime.today()
    mes = hoje.month

    data = models.DateField(blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    valor = models.CharField(max_length=50, blank=False)
    parcelamento = models.CharField(max_length=4, blank=False, default=1)       
    cartao = models.ForeignKey(CartaoDeCredito, on_delete=models.PROTECT)
    fatura = models.CharField(max_length=20, choices=CHOICE_MESES, default=mes)
    
    def __str__(self):
        return "{}: cartao: {} ({} - {})".format(self.data, self.cartao, self.valor, self.parcelamento)

class Caixa(models.Model):    
    hoje = datetime.datetime.now() 
    
    STATUS = {
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
    }
    
    MESES = {
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    }

    dia = models.CharField(max_length=2, default=hoje.day)      
    mes = models.CharField(max_length=15, choices=MESES, default=hoje.month)      
    ano = models.CharField(max_length=4, default=hoje.year)      
    descricao = models.CharField(max_length=150, blank=False, verbose_name='Descrição')
    valor = models.DecimalField(decimal_places=2, max_digits=8, blank=False)
    forma_de_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT, verbose_name="Forma de Pagamento") 
    parcelamento = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=8, choices=STATUS, default='Pendente')



class Despesa(Caixa):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(CategoriaDespesa, on_delete=models.PROTECT, blank=False)    
    def __str__(self):
        return "{}/{}/{}: {} - {} (R$ {})".format(self.dia, self.mes, self.ano, self.fornecedor, self.descricao, self.valor)
        
class Receita(Caixa):
    categoria = models.ForeignKey(CategoriaReceita, on_delete=models.PROTECT, blank=False)
    def __str__(self):
        return "{}/{}/{}: {} - R$ {}".format(self.dia, self.mes, self.ano, self.descricao, self.valor)