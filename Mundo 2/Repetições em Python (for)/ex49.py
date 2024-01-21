print("Esse programa escreve a tabuada para você!")

numero = int(input("Digite o número desejado: "))

for c in range(1, 10 + 1):
    print(f"{numero} x {c:2} = {numero*c}")
