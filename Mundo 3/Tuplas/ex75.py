valores = (int(input("Digite um número: ")),int(input("Digite um número: ")),
           int(input("Digite um número: ")),int(input("Digite um número: ")))

print(f"Você digitou os valores: {valores}")

print(f"O número 9 apareceu {valores.count(9)} vezes")

if 3 in valores:
    print(f"O número 3 foi digitado pela primeira vez na posição {valores.index(3)+1}")
else:
    print("Não há o número 3 na Tupla...")

print("Os números pares são:", end=" ")
for pos, num in enumerate(valores):
    if num % 2 == 0:
        print(num, end='')
