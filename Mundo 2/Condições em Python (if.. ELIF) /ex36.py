# Aprovar um empréstimo bancário para a compra de uma casa.
print("=" * 60)
print("Seja bem vindo ao programa de Empréstimo sua casa meu bolso cheio")
print("=" * 60)

# Perguntar o valor da casa (float)
valorCasa = float(input("Qual o valor da casa que irá comprar? R$"))
print("=" * 60)

# Perguntar o salário do comprador (float)
salario = float(input("Informe o seu salário: R$"))
print("=" * 60)

# Em quantos anos ele vai pagar (int)
anos = int(input("Em quantos anos irá pagar? "))
print("=" * 60)

# Calcular o valor da prestação mensal, ou seja, valor da casa / (anos*12)
prestMensal = valorCasa / (anos * 12)
print("O valor da prestação mensal é de R${:.2f}".format(prestMensal))
print("=" * 60)

# A prestação não pode exceder 30% do salário do cliente.
# 30% do salário = salario * 30/100


if prestMensal <= 30 / 100 * salario:
    print(
        f"Parabéns, você pode comprar a casa, irão sobrar R${salario - prestMensal:.2f} do seu salário"
    )
else:
    print("Você não pode comprar essa casa ainda.")
