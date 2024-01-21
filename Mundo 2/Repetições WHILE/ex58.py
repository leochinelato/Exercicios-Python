from random import randint

num = randint(0, 10)
numUser = 11
tentativas = 0

while numUser != num:
    numUser = int(input("Adivinhe o número de 0 a 10 que a máquina está pensando: "))
    tentativas += 1

print(f"Parabéns, você conseguiu com {tentativas} tentativas.")