# Leia o comprimento de três retas.
ab = float(input("Digite o comprimento da primeira reta (AB): "))
cd = float(input("Digite o comprimento da segunda reta (CD): "))
ef = float(input("Digite o comprimento da terceira reta (EF): "))

# Diga ao usuário se elas podem formar ou não um triangulo.

# AB = 16
# CD = 20
# EF = 30

# AB + CD > EF
# AB + EF > CD
# EF + CD > AB

if ab + cd > ef and ab + ef > cd and ef + cd > ab:
    print("Podem formar um triangulo")
else:
    print("Não podem formar um triangulo")
