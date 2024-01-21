# Leia um número inteiro e mostre se ele é PAR ou IMPAR

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O número {} é impar".format(num))
