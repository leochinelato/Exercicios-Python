# Leia idades e sexo de varias pessoas.
# Cada pessoa cadastrada será perguntado se ele quer continuar.

# Mostrar no final:
"""
Quantas pessoas tem mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres tem menos de 20 anos.
"""

mais18 = homens = mulherMenos20 = 0

while True:
    print("=" * 20)
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").upper()
    print("=" * 20)

    opcao = input("Deseja continuar? [S/N]: ").lower()

    if idade > 18:
        mais18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulherMenos20 += 1

    if opcao == "n":
        break

print(f"{mais18} pessoas têm mais de 18 anos.")
print(f"{homens} homens foram cadastrados.")
print(f"{mulherMenos20} mulheres tem menos de 20 anos")
