from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse

from .modules.ModuleHomePage import ModuleHomePage
from .modules.InsertOperacao import InsertOperacao


# Create your views here.
def home_page(request):
    lista_carteiras = ModuleHomePage(request).lista_carteiras()
    if request.method == "GET":
        return render(request, 'app_controle_ir/inserir_ativo.html', {
            'listaCarteiras': lista_carteiras
        })

    elif request.method == "POST":
        print(request.POST)
        module = ModuleHomePage(request)
        id_ativo = module.recuperar_id_pelo_nome_ativo()
        if id_ativo is None:
            return module.erro_recuperar_id_ativo('app_controle_ir/inserir_ativo.html')

        insert = InsertOperacao(request.POST, id_ativo).validarDados()
        if insert:
            return module.sucesso_inserir_ativo('app_controle_ir/inserir_ativo.html')
        else:
            return module.erro_inserir_ativo('app_controle_ir/inserir_ativo.html')


def success_action(request):
    return render(request, 'app_controle_ir/success_save.html')
