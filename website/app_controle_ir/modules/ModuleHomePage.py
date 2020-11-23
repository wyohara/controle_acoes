from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse, render, redirect

from ..models import Carteira
from ..models import Ativo


class ModuleHomePage:
    def __init__(self, request):
        self.__request = request
        self.__carteiras = Carteira.objects.all()

    def lista_carteiras(self):
        lista_carteiras = []
        for c in self.__carteiras:
            lista_carteiras.append({
                'id': c.id_carteira,
                'nome': c.nome,
            })
        return lista_carteiras

    def recuperar_id_pelo_nome_ativo(self):
        try:
            nome = self.__request.POST['nome_ativo'].upper()
            ativo = Ativo.objects.get(nome=nome)
            return ativo.id_ativo
        except ObjectDoesNotExist:
            return None

    def erro_recuperar_id_ativo(self, template):
        return render(self.__request, template, {
            'listaCarteiras': self.lista_carteiras(),
            'data_form': self.dados_formulario(),
            'error_ativo': "Ativo não existe"
        })

    def erro_inserir_ativo(self, template):
        return render(self.__request, template, {
            'listaCarteiras': self.lista_carteiras(),
            'data_form': self.dados_formulario(),
            "error": "Erro ao inserir o ativo"
        })

    def sucesso_inserir_ativo(self, template):
        return redirect(reverse('success_save'))

    def dados_formulario(self):
        return {
            'carteira_selec': self.__request.POST['carteira_selec'],
            'nome_ativo': self.__request.POST['nome_ativo'],
            'cotas': self.__request.POST['cotas'],
            'valor': self.__request.POST['valor'],
            'data': self.__request.POST['data'],
            'acao_realizada' + self.__request.POST['acao_realizada']: 'checked'
        }
