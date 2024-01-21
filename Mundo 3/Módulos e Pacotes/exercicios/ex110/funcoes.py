def texto(msg):
    print("=" * 30)
    print(f"{msg}".center(30))
    print("=" * 30)


def resumo(v, a, r):
    texto("RESUMO DO VALOR")
    print(f"Preço analisado: \t{moeda(v)}")
    print(f"Dobro do preço: \t{moeda(dobro(v))}")
    print(f"Metade do preço: \t{moeda(metade(v))}")
    print(f"{a}% de aumento: \t{moeda(aumentar(v,a))}")
    print(f"{r}% de redução: \t{moeda(diminuir(v,r))}")
    print("=" * 30)


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
