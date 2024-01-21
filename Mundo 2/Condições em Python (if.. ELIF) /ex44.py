'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

'''

valorProduto = float(input("Digite o valor do produto: R$"))

print("="*50)
print("Selecione uma das opções abaixo: ")
print("(1) à vista (dinheiro ou cheque)")
print("(2) à vista (cartão)")
print("(3) em até 2x no cartão")
print("(4) 3x ou mais no cartão")

selecao = int(input("Selecione: "))

if selecao == 1:
    valorFinal = valorProduto - (valorProduto*10/100)
    print("Você teve um desconto de 10%")
elif selecao == 2:
    valorFinal = valorProduto - (valorProduto*5/100)
    print("Você teve um desconto de 5%")
elif selecao == 3:
    valorFinal = valorProduto
    print("Você não recebeu desconto na compra")
elif selecao == 4:
    valorFinal = valorProduto + (valorProduto*20/100)
    print("O juros foi de 20% na compra")
else:
    print("="*50)
    print("Selecione uma das opções abaixo: ")
    print("(1) à vista (dinheiro ou cheque)")
    print("(2) à vista (cartão)")
    print("(3) em até 2x no cartão")
    print("(4) 3x ou mais no cartão")

    selecao = int(input("Selecione: "))

print(f"O valor final é de: R${valorFinal:.2f}")