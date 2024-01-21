cont = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input("Digite um número: "))
    if numero != 999:
        cont += 1
        soma += numero

print(f"A soma entre os {cont} números digitados é igual a: {soma}")
