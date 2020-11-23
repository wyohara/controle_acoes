from ..models import Ativo, Carteira, Operacao
from .InsertAtivoCarteira import InsertAtivoCarteira
from .FormOperacao import FormOperacao


class InsertOperacao:
    def __init__(self, postRequest, id_ativo):
        self.__id_ativo = id_ativo
        self.__post_request = postRequest.copy()
        self.__operacao_inserida = None
        self.__valor = float(postRequest['valor'])
        self.__cotas = int(postRequest['cotas'])
        self.__tipo_operacao = self.parse_tipo_operacao()
        print(self.__tipo_operacao)
        self.__carteira_selec = int(self.__post_request['carteira_selec'])

    def parse_tipo_operacao(self):
        if self.__post_request['acao_realizada'] == "0":
            return False
        else:
            return True

    def validarDados(self):
        self.__post_request["lucro_ou_perda"] = InsertAtivoCarteira.definir_lucro_ou_perda()
        self.__post_request['acao_realizada'] = self.parse_tipo_operacao()
        self.__post_request['fk_ativos_id'] = Ativo.objects.get(id_ativo=self.__id_ativo)
        self.__post_request['fk_carteira_id'] = Carteira.objects.get(id_carteira=int(self.__post_request['carteira_selec']))

        form = FormOperacao(self.__post_request)
        if form.is_valid():
            self.montar_dados_ativo_carteira(form.save().id_operacao)
            return True
        else:
            return False

    def montar_dados_ativo_carteira(self, id_operacao):
        operacao = Operacao.objects.get(id_operacao=id_operacao)
        ativo = InsertAtivoCarteira(operacao).atualizar_tabela_carteira_ativo(self.__id_ativo, self.__carteira_selec)
