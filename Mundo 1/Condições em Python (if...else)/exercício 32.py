from datetime import date

# Leia um ano e diga se é bissexto.

ano = int(input("Digite um ano ou coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto (tem 366 dias)".format(ano))
else:
    print("O ano de {} não é bissexto (tem 365 dias)".format(ano))
