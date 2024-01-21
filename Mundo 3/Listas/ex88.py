from random import randint

numJogos = int(input("Digite a qtd de jogos: "))
lista = list()
jogos = list()
posJogoPrint = 1

for q in range(numJogos):
    cont = 0
    while True:
        numGerado = randint(1, 60)
        if numGerado not in lista:
            lista.append(numGerado)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for jogo in jogos:
    print(f"Jogo {posJogoPrint}: {jogo}")
    posJogoPrint += 1