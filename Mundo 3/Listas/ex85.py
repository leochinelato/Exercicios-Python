lista = [[], []]
listaTemp = list()

for c in range(0, 7):
    listaTemp.append(int(input("Digite o valor: ")))

for v in listaTemp:
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)

lista[0].sort()
lista[1].sort()

print(f"Lista completa: {lista}")
print("=" * 40)
if len(lista[0]) <= 0:
    print("Não houveram números pares...")
else:
    print(f"Lista par: {lista[0]}")

print("=" * 40)

if len(lista[1]) <= 0:
    print("Não houveram números ímpares...")
else:
    print(f"Lista ímpar: {lista[1]}")
