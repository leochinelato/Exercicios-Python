# Funcionamento de um caixa eletrônico.
# Perguntar qual valor será sacado (inteiro)
# Vai informar quantas cédulas de cada valor serão entregues.

# obs: O caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 30)
print("{:^30}".format("BANCO LEO"))
print("=" * 30)

valor = int(input("Qual valor você quer sacar? R$"))
total = valor
cedAtual = 50
totalCed = 0

while True:
    if total >= cedAtual:
        total -= cedAtual
        totalCed += 1
    else:
        print(f"Total de {totalCed} cédulas de R${cedAtual}")
        if cedAtual == 50:
            cedAtual = 20
        elif cedAtual == 20:
            cedAtual = 10
        elif cedAtual == 10:
            cedAtual = 1
        totalCed = 0

        if total == 0:
            break
