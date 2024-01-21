from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
jogadores = {
    "Jogador1": randint(1, 6),
    "Jogador2": randint(1, 6),
    "Jogador3": randint(1, 6),
    "Jogador4": randint(1, 6),
}
print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("== RANKING DOS JOGADORES ==")
for pos, v in enumerate(ranking):
    print(f"{pos+1}° Lugar: {v[0]} com {v[1]}")
