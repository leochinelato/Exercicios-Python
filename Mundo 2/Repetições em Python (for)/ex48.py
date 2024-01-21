# Calcule a soma entre os ímpares
# Que são multiplos de 3
# Intervalo de 1 ate 500
soma = 0
cont = 0

for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f"A soma de todos os {cont} valores solicitados é: {soma}")
