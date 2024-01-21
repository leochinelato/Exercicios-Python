def ficha(nomeJogador="", golsMarcados=0):
    if golsMarcados > 1:
        print(f"O jogador {nomeJogador} fez {golsMarcados} gols no campeonato.")
    else:
        print(f"O jogador {nomeJogador} fez {golsMarcados} gol no campeonato.")


jogador = str(input("Digite o nome do jogador: ").strip())
gols = str(input("Digite o número de gols: ").strip())

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if len(jogador) == 0:
    jogador = "Desconhecido"

ficha(jogador, gols)

print("teste")