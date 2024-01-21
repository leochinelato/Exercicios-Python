# Ler o primeiro termo da PA
# Ler a razão

# Primeiro termo = 2
# Razão = 1

# Mostrar os primeiros 10:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

priTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

count = 1

while count <= 10:
    termo = priTermo + (count - 1) * razao
    count += 1
    print(termo, end="➡️")
print("Acabou")