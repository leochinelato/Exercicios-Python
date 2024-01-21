priTermo = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for c in range(1, 10 + 1):
    termo = priTermo + (c - 1) * r
    print(termo, end="➡️")
print("Acabou!")
