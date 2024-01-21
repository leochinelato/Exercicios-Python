valores = []

for c in range(0, 6):
    valores.append(int(input("Digite um número: ")))

    if c == 0:
        maiorValor = menorValor = valores[c]
        posicaoMaior = posicaoMenor = c
    else:
        if valores[c] > maiorValor:
            maiorValor = valores[c]
            posicaoMaior = c
        if valores[c] < menorValor:
            menorValor = valores[c]
            posicaoMenor = c

for n in valores:
    print(n, end="...")

print(f"\nO maior valor digitado foi: {maiorValor} na posição {posicaoMaior}")
print(f"O menor valor digitado foi: {menorValor} na posição {posicaoMenor}")
