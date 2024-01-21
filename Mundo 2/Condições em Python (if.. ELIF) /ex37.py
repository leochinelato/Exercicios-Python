# Programa que le um número inteiro e dê 3 opções pro user:

# converter para binário
# converter para octal
# converter para hexadecimal

print("=" * 60)
print("Seja bem vindo ao conversor inteligente")
print("=" * 60)


numero = int(input("Digite um número: "))

print("Qual será a base de conversão? Escolha uma opção")
print("(1) Para Binário")
print("(2) Para Octal")
print("(3) Para Hexadecimal")

escolha = int(input("Escolha: "))

if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
elif escolha == 3:
    print(hex(numero))
