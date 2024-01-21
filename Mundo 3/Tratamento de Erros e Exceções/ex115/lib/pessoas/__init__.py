from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("\033[31mERRO na criação\033[m")
    else:
        print("\033[32mArquivo criado.\033[m")
    finally:
        a.close()


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("ERRRO ao ler arquivo.")
    else:
        titulo("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        print(a.read())


def cadastrar(arquivo, nome="desconhecido", idade=0):
    try:
        a = open(arquivo, "at")
    except:
        print("HOUVE UM ERRO NA ABERTURA")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("HOUVE UM ERRO AO ESCREVER OS DADOS.")
        else:
            print(f"{nome} adicionado!")
            a.close()
    finally:
        a.close()
