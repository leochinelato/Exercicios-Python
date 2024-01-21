# Pergunte a distância de uma viagem em KM.
distViagem = float(input("Digite a distância em KM da viagem: "))

# Calcule o preço da passagem.
# R$ 0.50 por Km se a viagem for até 200km.
# R$ 0.45 para viagens acima de 200km.

if distViagem <= 200:
    preco = distViagem * 0.5
else:
    preco = distViagem * 0.45

print("O preço da viagem de {}KM é de: R${}".format(distViagem, preco))
