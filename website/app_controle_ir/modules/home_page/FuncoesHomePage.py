from django.core.exceptions import ObjectDoesNotExist
from ...models import Carteira
from ...models import Ativo


class FuncoesHomePage:
    def __init__(self, request):
        self.__request = request
        self.__carteiras = Carteira.objects.all()

    def gerar_lista_carteiras(self):
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