# [ valores[0,0] ] [ valores[0,1] ] [ valores[0,2] ]
# [ valores[1,0] ] [ valores[1,1] ] [ valores[1,2] ]
# [ valores[2,0] ] [ valores[2,1] ] [ valores[2,2] ]

# usuário digitar 9 números, 3 para cada lista dentro da lista principal.

valores = [[], [], []]
for pos, v in enumerate(valores):
    for c in range(0, 3):
        # print(pos, c)
        valores[pos].insert(c, int(input(f"Digite o valor da posição {pos},{c}: ")))
for c in range(0, 3):
    for v in range(0, 3):
        print(f"[ {valores[c][v]} ]", end="")
    print()
