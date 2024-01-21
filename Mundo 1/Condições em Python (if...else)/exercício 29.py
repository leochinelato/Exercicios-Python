# Leia a velocidade de um carro.
velo = float(input("Digite a velocidade que o carro está: "))


# Se ele ultrapassar 80km/h mostre:
# VOCÊ FOI MULTADO

# opcao 1

# veloMulta = 80
# if velo > veloMulta:
#     print("Você foi multado, a multa será de {}".format( (velo - veloMulta) * 7 ))

# A multa será de R$ 7 por cada Km acima do limite.

# opcao 2

if velo > 80:
    print("MULTADO!, o limite é 80km/h")
    multa = (velo - 80) * 7
    print("Você deve pagar R${:.2f} de multa".format(multa))
