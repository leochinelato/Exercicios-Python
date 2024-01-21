# ler o preço do produto
precoInicial = float(input("Digite o preço do produto: R$"))

# fazer a conta do preço -5%
precoFinal = precoInicial - (precoInicial*5/100)

# imprimir o preço novo
print("O produto com 5% de desconto custa R${:.2f}".format(precoFinal))