def moeda(v, moeda="R$"):
    return f"{moeda}{v:.2f}".replace(".", ",")


def dobro(v):
    return v * 2


def metade(v):
    return v / 2


def aumentar(v=0, por=0):
    v += (por / 100) * v
    return v


def diminuir(v=0, por=0):
    v -= (por / 100) * v
    return v
