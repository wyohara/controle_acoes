from ..models import Ativo, Carteira, Operacao
from ..forms.FormOperacao import FormOperacao
from .home_page.MensagensHomePage import MensagensHomePage


class InsertOperacao:
    def __init__(self, postRequest, id_ativo):
        self.__id_ativo = id_ativo
        self.__post_request = postRequest.POST.copy()
        self.__form = None
        self.__msg_formulario = MensagensHomePage(postRequest)

    def validar_dados(self, template):
        self.__post_request["lucro_ou_perda"] = 0
        self.__post_request['acao_realizada'] = self.__parse_tipo_operacao()
        self.__post_request['fk_ativos_id'] = Ativo.objects.get(id_ativo=self.__id_ativo)
        self.__post_request['fk_carteira_id'] = Carteira.objects.get(
            id_carteira=int(self.__post_request['carteira_selec']))

        form = FormOperacao(self.__post_request)
        if form.is_valid():
            self.salvar_operacao(self.__post_request['fk_ativos_id'],
                                 self.__post_request['fk_carteira_id'], form)
            if int(self.__post_request["cotas"]) == 0 or float(self.__post_request["valor"]) == 0.0:
                return self.__msg_formulario.erro_campo_vazio(template)
            return self.__msg_formulario.sucesso_inserir_ativo()

        else:
            return self.__msg_formulario.erro_inserir_ativo(template)

    def salvar_operacao(self, ativo, carteira, form_operacao):
        id_operacao = form_operacao.save().id_operacao

        operacao_inserida = Operacao.objects.get(id_operacao=id_operacao)
        compra = True
        operacoes = Operacao.objects.filter(fk_ativos_id=ativo, fk_carteira_id=carteira).order_by('data')
        cotas_totais = 0
        valor_total = 0.0
        for operacao in operacoes:
            if operacao.data <= operacao_inserida.data:
                if operacao.acao_realizada is compra:
                    cotas_totais += int(operacao.cotas)
                    valor_total += (float(operacao.valor) * operacao.cotas)
                elif operacao.acao_realizada is not compra:
                    cotas_totais -= int(operacao.cotas)
                    cotas_totais = abs(cotas_totais)  # prevenindo cotas com valor negativo
                    valor_total -= (float(operacao.valor) * operacao.cotas)

        operacao_inserida = self.__atualizar_operacao_inserida(cotas_totais, operacao_inserida, valor_total)
        operacao_inserida = self.__atualizar_lucro_ou_perda(compra, cotas_totais, operacao_inserida, valor_total)
        operacao_inserida.save()

    @staticmethod
    def __atualizar_operacao_inserida(cotas_totais_operacoes, operacao_inserida, valor_acumulado_operacoes):
        if cotas_totais_operacoes != 0:
            valor_medio = valor_acumulado_operacoes / cotas_totais_operacoes
        else:
            valor_medio = 0
        operacao_inserida.valor_medio = valor_medio
        operacao_inserida.cotas_totais = cotas_totais_operacoes
        return operacao_inserida

    @staticmethod
    def __atualizar_lucro_ou_perda(compra, cotas_totais_operacoes, operacao_inserida, valor_acumulado_operacoes):
        valor_medio = 0
        try:
            if operacao_inserida.acao_realizada is not compra:
                # revertendo os dados da operação inserida para gerar o lucro ou perda
                cotas_totais_operacoes += operacao_inserida.cotas
                valor_acumulado_operacoes += operacao_inserida.cotas * float(operacao_inserida.valor)
                valor_medio = valor_acumulado_operacoes / cotas_totais_operacoes
        except ZeroDivisionError:
            pass
        operacao_inserida.lucro_ou_perda = (float(operacao_inserida.valor) - valor_medio) * operacao_inserida.cotas
        return operacao_inserida

    def __parse_tipo_operacao(self):
        if self.__post_request['acao_realizada'] == "0":
            return False
        else:
            return True
