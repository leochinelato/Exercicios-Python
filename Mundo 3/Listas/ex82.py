opcao = "s"
valores = []
valoresPares = []
valoresImpares = []

while opcao in "Ss":
    valores.append(int(input("Digite um valor: ")))
    opcao = str(input("Deseja continuar? [S/N]: ")).strip()

for v in valores:
    if v % 2 == 0:
        valoresPares.append(v)
    else:
        valoresImpares.append(v)

print("="*40)
print(f"Lista de valores: {valores}")
print("="*40)
print(f"Valores Pares: {valoresPares}")
print("="*40)
print(f"Valores Ímpares: {valoresImpares}")