from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)

print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input("Qual é a sua jogada? "))

print("-="*12)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*12)

if computador == 0: # computador jogou pedra

    if jogador == 0: # jogador jogou pedra
        print("EMPATE!")
    elif jogador == 1: # jogador jogou papel
        print("VOCÊ VENCEU")
    elif jogador == 2: # jogador jogou tesoura
        print("VOCÊ PERDEU")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 1: # computador jogou papel
        
    if jogador == 0: # jogador jogou pedra
        print("VOCÊ PERDEU")
    elif jogador == 1: # jogador jogou papel
        print("EMPATE!")
    elif jogador == 2: # jogador jogou tesoura
        print("VOCÊ VENCEU")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 2: # computador jogou tesoura
        
    if jogador == 0: # jogador jogou pedra
        print("VOCÊ VENCEU")
    elif jogador == 1: # jogador jogou papel
        print("VOCÊ PERDEU")
    elif jogador == 2: # jogador jogou tesoura
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")

        