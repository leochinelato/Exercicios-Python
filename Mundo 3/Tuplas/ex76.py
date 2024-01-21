# tupla com nome de produtos e preços

produtos = ("Tablet", 1600, "Celular", 4300, "Notebook", 3500)

print("=" * 50)
print("{:^50}".format("LISTAGEM DOS PREÇOS"))
print("=" * 50)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f"{produtos[c]:.<30}", end="")
    else:
        print(f"R${produtos[c]:>4.2f}")
