from ..models import CarteiraAtivo, Carteira, Ativo, Operacao
from django.core.exceptions import ObjectDoesNotExist


class InsertAtivoCarteira:

    def __init__(self, operacao):
        self.carteira_ativo = None
        self.operacao = operacao

    @staticmethod
    def definir_lucro_ou_perda():
        return 0

    def atualizar_tabela_carteira_ativo(self, id_ativo, id_carteira):
        try:
            carteira_ativo = CarteiraAtivo.objects.get(fk_ativos_id=id_ativo,
                                                               fk_carteira_id=id_carteira)
            print(carteira_ativo.id_carteira_ativos)
            if self.operacao.acao_realizada:
                self.__compra_novos_ativos(carteira_ativo)
            else:
                self.__venda_ativos(carteira_ativo)

        except Exception as e:
            carteira_ativo = CarteiraAtivo.objects.create(valor_medio=self.operacao.valor, cotas=self.operacao.cotas,
                                         fk_carteira_id=Carteira.objects.get(id_carteira=id_carteira),
                                         fk_ativos_id=Ativo.objects.get(id_ativo=id_ativo))

    def __venda_ativos(self, carteira_ativo):
        operacao = self.operacao
        cotas_totais = carteira_ativo.cotas - operacao.cotas
        valor_total = (carteira_ativo.cotas * carteira_ativo.valor_medio) - (operacao.cotas * operacao.valor)
        valor_medio = valor_total / cotas_totais
        carteira_ativo.update(
            cotas=cotas_totais, valor_medio=valor_medio
        )

    def __compra_novos_ativos(self, carteira_ativo):
        operacao = self.operacao
        cotas_totais = carteira_ativo.cotas + operacao.cotas
        valor_total = (carteira_ativo.cotas * carteira_ativo.valor_medio) + (operacao.cotas * operacao.valor)
        valor_medio = valor_total / cotas_totais
        carteira_ativo.update(
            cotas=cotas_totais, valor_medio=valor_medio
        )