# Programa que leia o nome de uma cidade e diga se começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome de sua cidade: ")).strip()

# Forma 1

# cidadeDividida = cidade.split()

# primeiroNome = cidadeDividida[0]

# primeiroNomeLower = primeiroNome.lower()

# if ("santo" in primeiroNomeLower):
#     print("Começa com santo")
# else:
#     print("Não começa com santo")


# Forma 2

print(cidade[:5].upper() == "SANTO")