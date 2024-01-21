aluno = {}

aluno['Nome'] = str(input("Digite o nome do aluno: ")).strip()
aluno['Média'] = float(input("Digite a média do aluno: "))


if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'


for k, v in aluno.items():
    print(f"{k} - {v}")