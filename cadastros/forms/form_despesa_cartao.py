from django import forms
from django.forms import ModelForm
from cadastros.models import DespesaCartaoDeCredito

from datetime import datetime

class FormDespesaCartaoCredito(ModelForm):
    class Meta:
        dia = datetime.today().day
        mes = datetime.today().month
        ano = datetime.today().year
        data = "{}/{}/{}".format(dia, mes, ano)
        model = DespesaCartaoDeCredito

        fields = '__all__'
        widgets = {
            'data': forms.DateInput(
                    format='%d/%m/%Y',
                    attrs={
                        'type':'date', 
                        'class': 'form-control mb-3'
                    }                
            ),           
            'descricao': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'fornecedor': forms.Select(attrs={'class': 'form-select form-control mb-3'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'parcelamento': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'cartao': forms.Select(attrs={'class': 'form-select form-control mb-3'}),
        }
