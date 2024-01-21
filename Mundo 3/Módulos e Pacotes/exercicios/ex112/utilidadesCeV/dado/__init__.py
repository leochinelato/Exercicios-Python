from utilidadesCeV import moedas


def texto(msg):
    print("=" * (len(msg) + 4))
    print(f"  {msg}")
    print("=" * (len(msg) + 4))


def resumo(v, a, r):
    texto("RESUMO DO VALOR")
    print(f"Preço analisado:{moedas.moeda(v):>21}")
    print(f"Dobro:{moedas.moeda(moedas.dobro(v)):>31}")
    print(f"Metade:{moedas.moeda(moedas.metade(v)):>30}")
    print(f"{a}% de aumento:{moedas.moeda(moedas.aumentar(v,a)):>22}")
    print(f"{r}% de redução:{moedas.moeda(moedas.diminuir(v,r)):>22}")
    print("=" * 19)


def leiaDinheiro(msg):
    while True:
        v = str(input(msg))
        if v.isnumeric():
            v = float(v)
            break
        else:
            print(f"ERRO! '{v}' não é um valor númerico")
    return v
