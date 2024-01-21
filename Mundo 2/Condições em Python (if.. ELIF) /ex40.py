# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

aluno = str(input("Digite o nome do aluno: ")).strip()

nota1 = float(input(f"Digite a primeira nota do {aluno}: "))
nota2 = float(input(f"Digite a segunda nota do {aluno}: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("REPROVADO...")
elif media <= 6.9:
    print("Você está de recuperação...")
else:
    print("APROVADO! Parabéns.")

print(f"Sua média foi de {media}")