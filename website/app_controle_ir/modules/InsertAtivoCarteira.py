from ..models import CarteiraAtivo, Carteira, Ativo, Operacao
from django.core.exceptions import ObjectDoesNotExist


class InsertAtivoCarteira:

    def __init__(self, operacao):
        self.carteira_ativo = None
        self.operacao = operacao

    @staticmethod
    def definir_lucro_ou_perda():
        return 0
