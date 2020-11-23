from django import forms
from ..models import Operacao


class FormOperacao(forms.ModelForm):
    class Meta:
        model = Operacao
        fields = ['acao_realizada','cotas','lucro_ou_perda', 'valor', 'data', 'fk_ativos_id', 'fk_carteira_id']