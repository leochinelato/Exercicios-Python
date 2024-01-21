resposta = ""
numero = soma = cont = maior = menor = 0
while resposta in "Ss":
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    if numero > maior:
        maior = numero
    if cont == 1:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    resposta = str(input("Deseja continuar [S/N]: ")).strip()
media = soma / cont
print(f"A média entre os números digitados é de: {media:.2f}")
print(f"O maior valor digitado é: {maior}")
print(f"e o menor valor é: {menor}")
