from django.shortcuts import render
from .modules.home_page.FuncoesHomePage import FuncoesHomePage
from .modules.InsertOperacao import InsertOperacao
from .modules.home_page.MensagensHomePage import MensagensHomePage


# Create your views here.
def home_page(request):
    lista_carteiras = FuncoesHomePage(request).gerar_lista_carteiras()
    if request.method == "GET":
        return render(request, 'app_controle_ir/inserir_ativo.html', {
            'listaCarteiras': lista_carteiras
        })

    elif request.method == "POST":
        id_ativo_para_inserir = FuncoesHomePage(request).recuperar_id_pelo_nome_ativo()
        msg_home_page = MensagensHomePage(request)
        if FuncoesHomePage(request).recuperar_id_pelo_nome_ativo() is None:
            return msg_home_page.erro_recuperar_id_ativo('app_controle_ir/inserir_ativo.html')

        return InsertOperacao(request, id_ativo_para_inserir).validar_dados('app_controle_ir/inserir_ativo.html')


def success_action(request):
    return render(request, 'app_controle_ir/success_save.html')
