jogador = dict()
jogadores = list()
i = 0
while True:
    jogador["Cod"] = i
    jogador["Nome"] = str(input("Nome do Jogador: ")).strip()
    jogador["Partidas"] = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    jogador["Gols"] = []
    jogador["TotGols"] = 0
    for c in range(jogador["Partidas"]):
        jogador["Gols"].append(int(input(f" Quantos gols fez na partida {c+1}: ")))
    for gol in jogador["Gols"]:
        jogador["TotGols"] += gol
    jogadores.append(jogador.copy())
    resp = str(input("Deseja continuar? [S/N] "))
    i += 1
    if resp in "nN":
        break
print("-=" * 30)
for i in jogador.keys():
    print(f"{i:<15}", end="")
print("=-" * 30)
for k, v in enumerate(jogadores):
    print(f"{k:>3}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
iJogador = 0
while True:
    iJogador = int(input("Mostrar dados de qual jogador? (999 para sair): "))
    if iJogador != 999:
        if iJogador > len(jogadores) - 1:
            print("Jogador não encontrado...")
        else:
            print(f"LEVANTAMENTO DO JOGADOR {jogadores[iJogador]['Nome']}: ")
            for c in range(jogadores[iJogador]["Partidas"]):
                print(f"No jogo {c} fez {jogadores[iJogador]['Gols'][c]} gols.")
    else:
        print("Saindo...")
        break
