from utilidadesCeV import moedas


def texto(msg):
    print("=" * 30)
    print(f"{msg}".center(30))
    print("=" * 30)


def resumo(v, a, r):
    texto("RESUMO DO VALOR")
    print(f"Preço analisado: {moedas.moeda(v)}")
    print(f"Dobro:           {moedas.moeda(moedas.dobro(v))}")
    print(f"Metade:          {moedas.moeda(moedas.metade(v))}")
    print(f"{a}% de aumento:  {moedas.moeda(moedas.aumentar(v,a))}")
    print(f"{r}% de redução:  {moedas.moeda(moedas.diminuir(v,r))}")
    print("=" * 30)
