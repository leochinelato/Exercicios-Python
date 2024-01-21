# Programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input("Digite o seu nome: ")).strip()


# Forma 1

# nomeLower = nome.lower()

# if ("silva" in nomeLower):
#     print("Seu nome tem silva")
# else:
#     print("Seu nome não tem silva")

# Forma 2

print("Seu nome tem Silva? {}".format("silva" in nome.lower()))