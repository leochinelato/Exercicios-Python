# Pergunte o salário do funcionário.
salario = float(input("Digite o salário do funcionário: R$"))

# Salários acima de R$ 1250, aumento de 10%.
# Salários abaixo disso, aumento de 15%.

if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)

print(
    "O salário do colaborador de R${:.2f} com aumento é de: R${:.2f}".format(
        salario, novo
    )
)
