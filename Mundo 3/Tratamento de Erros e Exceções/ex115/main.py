from lib.interface import *
from lib.pessoas import *

arquivo = "pessoas.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(
        ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"]
    )
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        titulo("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        titulo("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
