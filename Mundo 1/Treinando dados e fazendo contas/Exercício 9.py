print("Esse programa escreve a tabuada para você")

numero = int(input("Digite um número: "))

counter = 1
while counter <= 10:
    print("{} x {:2} = {}".format(numero,counter, (counter*numero) ))
    counter += 1