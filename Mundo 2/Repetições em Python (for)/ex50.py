soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input(f"Digite o {c}° número: "))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f"Dos números informados, {cont} são pares, e a soma entre eles é de: {soma}")
