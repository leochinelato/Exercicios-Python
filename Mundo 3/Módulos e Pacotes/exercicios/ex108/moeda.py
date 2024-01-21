def aumentar(num=0, por=0):
    num += (por / 100) * num
    return num


def diminuir(num=0, por=0):
    num -= (por / 100) * num
    return num


def dobro(num=0):
    return num * 2


def metade(num=0):
    return num / 2


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:.2f}".replace(".", ",")
