"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM

Até 14 anos: INFANTIL

Até 19 anos: JÚNIOR

Até 25 anos: SÊNIOR

Acima de 25 anos: MASTER
"""
import datetime

print("=" * 50)
print("Seja bem vindo a Confederação nacional de natação")
print("=" * 50)

anoNascimento = int(input("Digite o ano de seu nascimento: "))
anoAtual = datetime.date.today().year
idadeAtleta = anoAtual - anoNascimento

if idadeAtleta <= 9:
    categoria = "MIRIM"
elif idadeAtleta <= 14:
    categoria = "INFANTIL"
elif idadeAtleta <= 19:
    categoria = "JÚNIOR"
elif idadeAtleta <= 25:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print(f"Você tem {idadeAtleta} anos, sua categoria é {categoria}")
