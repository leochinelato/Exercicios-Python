# Fazer o professor digitar quatro usuários

# Sortear um dos usuários para apagar o quadro

# Precisa imprimir o nome do escolhido

from random import choice

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

alunoSortudo = choice(lista)

print("O aluno escolhido foi: ".format(alunoSortudo))