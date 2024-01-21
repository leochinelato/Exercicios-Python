# FORMA MAIS FÁCIL:
"""
from math import factorial

print("=-"*20)
print("Seja bem-vindo a sua calculadora de fatorial!")
numero = int(input("Digite um número: "))
print("=-"*20)

print(f"Resultado: {factorial(numero)}")

"""

numero = int(input("Digite um número para calcular fatorial: "))
c = numero
f = 1

print(f"Calculando {numero}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
