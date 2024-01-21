def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def moeda(n, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".", ",")
