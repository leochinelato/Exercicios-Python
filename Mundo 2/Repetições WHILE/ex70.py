# Ler o nome e preço de vários produtos.
# Perguntar se o usuário quer continuar.

# Mostrar:
"""
Total gasto na compra.
Quantos produtos custam mais de R$1000
Qual o nome do produto mais barato.
"""

totalGasto = produtosMaisMil = 0

count = 1

while True:
    nomeProduto = input("Digite o nome do produto: ").lower().strip()
    precoProduto = int(input("Digite o preço do produto: R$"))

    if count == 1:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto
        count += 1

    totalGasto += precoProduto

    if precoProduto >= 1000:
        produtosMaisMil += 1

    if precoProduto < precoMaisBarato:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto

    opcao = input("Deseja continuar? [S/N]: ").upper()

    if opcao == "N":
        print("Fechando...")
        break

print("="*60)
print(f"O total gasto foi de: R${totalGasto}")
print(f"{produtosMaisMil} produtos custaram mais de R$1000")
print(f"{produtoMaisBarato} é o produto mais barato, custando R${precoMaisBarato}")
print("="*60)