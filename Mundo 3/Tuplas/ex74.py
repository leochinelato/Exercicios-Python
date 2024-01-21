from random import randint

numerosAleatorios = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
)

print(numerosAleatorios)

print(f'O maior valor foi: {max(numerosAleatorios)}')
print(f'O menor valor foi: {min(numerosAleatorios)}')

# maiorNum = numerosAleatorios[0]
# menorNum = numerosAleatorios[0]

# for pos, num in enumerate(numerosAleatorios):
#     if numerosAleatorios[pos] > maiorNum:
#         maiorNum = numerosAleatorios[pos]
#     if numerosAleatorios[pos] < menorNum:
#         menorNum = numerosAleatorios[pos]

# print(f"O maior número é {maiorNum} e o menor é {menorNum}")
