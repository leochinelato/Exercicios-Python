from datetime import date

maiores = 0
menores = 0

for c in range(1, 8):
    anoNasc = int(input(f"Digite o ano de nascimento da pessoa {c}: "))
    anoAtual = date.today().year
    if anoAtual - anoNasc >= 21:
        maiores += 1
    else:
        menores += 1

print(f"{maiores} pessoas são maiores de idade")
print(f"{menores} pessoas são menores de idade")
