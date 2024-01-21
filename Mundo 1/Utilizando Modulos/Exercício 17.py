import math

# ler o comprimento do cateto oposto do triangulo
catetoOposto = float(input("Cateto Oposto: "))

# ler o comprimento do cateto adjacente do triangulo
catetoAdjacente = float(input("Cateto Adjacente: "))

# calcular e mostrar o comprimento da hipotenusa
# h = raiz da soma dos catetos ao quadrado

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print("A hipotenusa é: {:.2f}".format(hipotenusa))