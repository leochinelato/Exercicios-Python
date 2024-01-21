# Leia o ano de nascimento do jovem (int)

# De acordo com sua idade:
# Se ele ainda vai se alistar.          Menos de 18 anos.
# Se é a hora de se alistar.            Exatos 18 anos.
# Se já passou do tempo do alistamento. Maior de 18 anos.

# Deve mostrar o tempo(anos) que falta ou que passou do prazo.

import datetime

anoNascimento = int(input("Digite o ano do seu nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento

print("Você tem {} anos de idade".format(idade))

if idade < 18:
    print("Ainda irá se alistar! Faltam {} anos".format(18 - idade))
elif idade > 18:
    print("Já passou o prazo do alistamento há {} anos".format(idade - 18))
else:
    print("Está na hora de se alistar")
