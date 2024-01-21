# Jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER.

# Mostre o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:
    jogadorNumero = int(input("Jogue um número de 1 a 10: "))
    maquinaNumero = randint(1, 10)
    soma = jogadorNumero + maquinaNumero

    jogadorEscolha = " "

    while jogadorEscolha not in "PI":
        jogadorEscolha = str(input("Par ou impar? [P/I] ")).strip().upper()[0]

    print(
        f"Você jogou {jogadorNumero} e o computador {maquinaNumero}. Total de {soma}"
    )

    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    print("="*50)

    if jogadorEscolha == resultado:
        vitorias += 1
        print(f"Você ganhou!")
    else:
        print(f"Você perdeu!")
        break

print("=" * 50)
print(f"Você perdeu, o número de vitórias consecutivas foi de {vitorias}")
