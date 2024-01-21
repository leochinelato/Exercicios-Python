pessoas = list()
dados = list()
totpessoas = 0
peso = list()
maiorPeso = menorPeso = 0

opcao = "s"

while opcao in "Ss":
    dados.append(str(input("Digite o nome: ")).strip())
    dados.append(float(input("Digite o peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input("Deseja continuar? [S/N]: ")).strip()


for c in range(0, len(pessoas)):
    if c == 0:
        maiorPeso = menorPeso = pessoas[c][1]
    else:
        if pessoas[c][1] >= maiorPeso:
            maiorPeso = pessoas[c][1]
        if pessoas[c][1] <= menorPeso:
            menorPeso = pessoas[c][1]

print("=-"*40)
print(f"Cadastrou {len(pessoas)} pessoas")
print(f"Maior: {maiorPeso}Kg peso de: ", end="")

for p in pessoas:
    if p[1] == maiorPeso:
        print(f"[ {p[0]} ]", end="")
print()
print(f"Menor: {menorPeso}Kg peso de: ", end="")
for p in pessoas:
    if p[1] == menorPeso:
        print(f"[ {p[0]} ]", end="")