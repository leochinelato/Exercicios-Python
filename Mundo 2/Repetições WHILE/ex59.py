n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

opcao = 0

while opcao != 5:
    print(
        """
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa
    """
    )
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    elif opcao == 2:
        multi = n1 * n2
        print(f"{n1} * {n2} = {multi}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        else:
            print(f"O maior é {n2}")
    elif opcao == 4:
        print("Digite novos números: ")
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente Novamente")
    print("=-=" * 10)
