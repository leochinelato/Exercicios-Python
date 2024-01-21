tempo = int(input("Quantos anos tem seu carro? "))
estado = str(input("Qual estado você mora? ")).upper().strip()

estado20anos = ["AC", "MS", "PR", "RS", "SP"]
estado15anos = [
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "PA",
    "PB",
    "PI",
    "RJ",
    "RO",
    "SE",
]
estado30anos = ["TO", "SC"]


if estado in estado20anos:
    if tempo <= 20:
        print("Paga IPVA")
    else:
        print("Não paga IPVA")
elif estado in estado15anos:
    if tempo <= 15:
        print("Paga IPVA")
    else:
        print("Não paga IPVA")
else:
    if tempo <= 30:
        print("Paga IPVA")
    else:
        print("Não paga IPVA")

nota = 7

# Condição simples
if nota >= 6:
    print("vc passou!")

# Condição composta
if nota >= 6:
    print("vc passou!")
else:
    print("está de recuperação")

# Condição simplificada
print("vc passou" if nota >= 6 else "está de recuperação!")
