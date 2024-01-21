# Criar um programa que lê o nome completo da pessoa e mostre:
nome = input("Digite o seu nome completo: ").strip()

# O nome com todas as letras maíusculas.
print(nome.upper())

# Com todas minúsculas
print(nome.lower())

# Quantas letras tem ao todo (sem contar espaços)
print("O nome tem {} caracteres sem contar espaços".format( len( nome.replace(" ", "") ) ))


# Quantas letras tem o primeiro nome:

# 1 forma
nomeDividido = nome.split()
print("O primeiro nome é {} tem {} caracteres".format( nomeDividido[0], len(nomeDividido[0]) ))

# 2 forma
# print("Seu primeiro nome tem {} letras".format(nome.find(" ")))