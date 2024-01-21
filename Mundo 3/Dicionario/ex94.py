pessoa = dict()
pessoas = list()
media = soma = 0
while True:
    pessoa["Nome"] = str(input("Digite o nome: ")).strip()
    while True:
        pessoa["Sexo"] = str(input("Digite o sexo [M/F]: ")).strip()
        if pessoa["Sexo"] in "MmFf":
            break
        print("ERRO! Digite M ou F.")
    pessoa["Idade"] = int(input("Digite a idade: "))
    soma += pessoa["Idade"]
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input("Deseja continuar [S/N]: ")).strip()
        if resp in "SsNn":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp in "nN":
        break
media = soma / len(pessoas)
print("=" * 40)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print("=" * 40)
print(f"A média de idade do grupo é: {media}")
print("=" * 40)
print("Lista de mulheres:")
for pessoa in pessoas:
    if pessoa["Sexo"] in "Ff":
        for k, v in pessoa.items():
            print(f"{k}: {v}")
        print("-" * 40)
print("Lista de pessoas acima da média de idade: ")
for pessoa in pessoas:
    if pessoa["Idade"] > media:
        for k, v in pessoa.items():
            print(f"{k}: {v}")
        print("-" * 40)
