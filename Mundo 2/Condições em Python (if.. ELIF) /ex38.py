# Leia dois números inteiros (int)

# Compare-os e diga:
# O primeiro é maior que o segundo
# O segundo é maior que o primeiro
# Os dois são iguais

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print("O primeiro valor ({}) é maior que o segundo ({})".format(a, b))
elif b > a:
    print("O segundo valor ({}) é maior que o primeiro valor ({})".format(b, a))
else:
    print("Os números são iguais ({})".format(a))
