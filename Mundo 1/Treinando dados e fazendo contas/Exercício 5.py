cores = {
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m",
    "azul":"\033[34m",
    "roxo":"\033[35m",
    "ciano":"\033[36m",
    "cinza":"\033[37m",
    "limpa":"\033[m"
}

numero = int(input("Digite um número: "))

print("O sucessor do número {} é {}{}{} e o antecessor é {}{}{}".format(numero,cores["verde"],numero+1,cores["limpa"],cores["vermelho"],numero-1,cores["limpa"]))