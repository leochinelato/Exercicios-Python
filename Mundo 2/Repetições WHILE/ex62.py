opcao = 1

priTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

count = 1
quantTermos = 10

while quantTermos != 0:
    while count <= quantTermos:
        termo = priTermo + (count - 1) * razao
        count += 1
        print(termo, end="➡️")
    print("Deseja mostrar mais termos? ")
    quantTermos += int(input("Digite quantos: "))