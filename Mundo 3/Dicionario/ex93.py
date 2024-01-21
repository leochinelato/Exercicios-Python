jogador = dict()
jogador["Nome"] = str(input("Digite o nome do jogador: ")).strip()
jogador["qtdPartidas"] = int(input("Quantas partidas jogou: "))
print("Ok!")
jogador["Gols"] = list()
jogador["TotGols"] = 0
for c in range(jogador["qtdPartidas"]):
    jogador["Gols"].append(int(input(f"Quantos gols fez na partida {c+1}: ")))
for gol in jogador["Gols"]:
    jogador["TotGols"] += gol
print("=" * 30)
for k, v in jogador.items():
    print(f"{k}: {v}")
print("=" * 30)
print(f"O jogador {jogador['Nome']} jogou {jogador['qtdPartidas']} partidas.")
for c in range(jogador["qtdPartidas"]):
    print(f"Na partida {c+1}, fez {jogador['Gols'][c]} gols.")
print(f"Foi um total de {jogador['TotGols']} gols.")
