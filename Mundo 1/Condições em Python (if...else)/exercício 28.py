import random

# Computador sortear um número de 0 a 5.
num = random.randint(0, 5)

# O usuário precisa descobrir qual foi o número escolhido.
numUser = int(input("Adivinhe o número sorteado de 0 a 5... "))

# O programa irá escrever na tela se o usuário venceu ou perdeu.
if numUser == num:
    print("Você acertou o número")
else:
    print("Tente novamente")

print("O número correto era {}".format(num))
