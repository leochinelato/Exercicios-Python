from datetime import date

pessoa = dict()

pessoa["Nome"] = str(input("Digite o nome: ")).strip()
pessoa["AnoNasc"] = int(input("Digite o ano que nasceu: "))
pessoa["CTPS"] = int(input("Digite a sua carteira de trabalho (0 não tem): "))
pessoa["Idade"] = date.today().year - pessoa["AnoNasc"]
if pessoa["CTPS"] != 0:
    print("Você já trabalhou!")
    pessoa["AnoContrat"] = int(input("Digite o ano de contratação: "))
    pessoa["Salário"] = float(input("Digite o seu salário: "))
    pessoa["AnoAposentado"] = pessoa["Idade"] + (
        (pessoa["AnoContrat"] + 35) - date.today().year
    )

for k, v in pessoa.items():
    print(f"{k}: {v}")
