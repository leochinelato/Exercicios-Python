valores = [[], [], []]
somaValores = somaTercoluna = maiorSegundaLinha = 0
for pos, v in enumerate(valores):
    for c in range(0, 3):
        # print(pos, c)
        valores[pos].insert(c, int(input(f"Digite o valor da posição [{pos}][{c}]: ")))
        somaValores += valores[pos][c]
        if c == 2:
            somaTercoluna += valores[pos][c]
        if pos == 1:
            if valores[pos][c] > maiorSegundaLinha:
                maiorSegundaLinha = valores[pos][c]
for c in range(0, 3):
    for v in range(0, 3):
        print(f"[ {valores[c][v]} ]", end="")
    print()
print("=" * 40)
print(f"A soma de todos os valores digitados é: {somaValores}")
print("=" * 40)
print(f"A soma da terceira coluna é: {somaTercoluna}")
print("=" * 40)
print(f"O maior valor da segunda linha é: {maiorSegundaLinha}")
print("=" * 40)
