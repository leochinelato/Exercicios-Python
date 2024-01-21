"""

Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

 EQUILÁTERO: todos os lados iguais

 ISÓSCELES: dois lados iguais, um diferente

 ESCALENO: todos os lados diferentes

"""

ab = float(input("Digite o comprimento da primeira reta (AB): "))
cd = float(input("Digite o comprimento da segunda reta (CD): "))
da = float(input("Digite o comprimento da terceira reta (DA): "))

tipoTri = " "

if ab + cd > da and ab + da > cd and da + cd > ab:
    print("Podem formar um triangulo")

    if ab == cd and cd == da:
        tipoTri = "Equilatero"
    elif ab != cd and cd != da:
        tipoTri = "Escaleno"
    else:
        tipoTri = "Isósceles"

    print(f"O tipo do triângulo é {tipoTri}")

else:
    print("Não podem formar um triangulo")
