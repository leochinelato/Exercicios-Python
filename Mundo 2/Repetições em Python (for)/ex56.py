somaIdades = 0
maiorIdade = 0
homemVelho = ""
mulheresMenos20 = 0

for c in range(1, 5):
    print(f"------- {c} PESSOA -------")
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo (M/F): ")).strip()
    somaIdades += idade
    print("=-" * 30)
    if sexo in "Mm":
        if idade > maiorIdade:
            homemVelho = nome
    if sexo in "Ff":
        if idade < 20:
            mulheresMenos20 += 1

print(f"A média de idade do grupo é: {somaIdades/4:.2f}")
print(f"O nome do homem mais velho é: {homemVelho}")
print(f"Têm {mulheresMenos20} mulheres menores de 20 anos")
