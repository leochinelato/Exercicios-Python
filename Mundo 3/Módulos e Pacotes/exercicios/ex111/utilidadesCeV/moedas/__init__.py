def moeda(v, moeda="R$"):
    return f"{moeda}{v}".replace(".", ",")


def dobro(v, formato=False):
    res = v * 2
    return res if not formato else moeda(v)


def metade(v, formato=False):
    res = v / 2
    return res if not formato else moeda(v)


def aumentar(v=0, por=0, formato=False):
    res = v + (por / 100) * v
    return res if not formato else moeda(v)


def diminuir(v=0, por=0, formato=False):
    res = v - (por / 100) * v
    return res if not formato else moeda(v)
