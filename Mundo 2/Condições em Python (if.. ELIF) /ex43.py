"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

 IMC abaixo de 18,5: Abaixo do Peso

 Entre 18,5 e 25: Peso Ideal

 25 até 30: Sobrepeso

 30 até 40: Obesidade

 Acima de 40: Obesidade Mórbida

"""

peso = float(input("Digite o seu peso: "))
alturaCM = float(input("Digite a sua altura (cm): "))
alturaM = alturaCM / 100

imc = peso / ((alturaM * alturaM))
status = " "

if imc < 18.5:
    status = "Abaixo do peso"
elif imc < 25:
    status = "Peso ideal"
elif imc < 30:
    status = "Sobrepeso"
elif imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"


print(f"Seu imc é de {imc:.2f}, você está: {status}")
