dinCarteira = float(input("Quantos reais há na sua carteira? R$"))

print("Com R${:.2f} você pode comprar US${:.2f}".format(dinCarteira, (dinCarteira/5.05)))