from django.shortcuts import reverse, render, redirect
from .FuncoesHomePage import FuncoesHomePage


class MensagensHomePage:
    def __init__(self, request):
        self.__request = request
        self.__lista_carteiras = FuncoesHomePage(request).gerar_lista_carteiras()

    def erro_campo_vazio(self, template):
        return render(self.__request, template, {
            'listaCarteiras': self.__lista_carteiras,
            'data_form': self.dados_formulario(),
            'error': "O campo cotas e valor não pode ser ZERO"
        })

    def erro_recuperar_id_ativo(self, template):
        return render(self.__request, template, {
            'listaCarteiras': self.__lista_carteiras,
            'data_form': self.dados_formulario(),
            'error_ativo': "Ativo não existe"
        })

    def erro_inserir_ativo(self, template):
        return render(self.__request, template, {
            'listaCarteiras': self.__lista_carteiras,
            'data_form': self.dados_formulario(),
            "error": "Erro ao inserir o ativo, campo inválido"
        })

    def sucesso_inserir_ativo(self):
        return redirect(reverse('success_save'))

    def dados_formulario(self):
        if self.__request.POST['acao_realizada'] == "0":
            checked = 'checked'
        else:
            checked = None

        return {
            'carteira_selec': self.__request.POST['carteira_selec'],
            'nome_ativo': self.__request.POST['nome_ativo'],
            'cotas': self.__request.POST['cotas'],
            'valor': self.__request.POST['valor'],
            'data': self.__request.POST['data'],
            'acao_realizada_venda': checked
        }