from ..models import Ativo, Carteira
from .InsertAtivoCarteira import InsertAtivoCarteira
from .FormOperacao import FormOperacao


class InsertOperacao:
    def __init__(self, postRequest, id_ativo):
        self.__id_ativo = id_ativo
        self.__post_request = postRequest.copy()

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
            id_operacao = form.save().id_operacao
            return True
        else:
            return False