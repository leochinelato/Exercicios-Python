import moeda

n = int(input("Digite um número: "))

print(f"{moeda.moeda(n)} + 10% é {moeda.moeda(moeda.aumentar(n,10))}")
print(f"{moeda.moeda(n)} - 20% é {moeda.moeda(moeda.diminuir(n,20))}")
print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}")
print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}")
