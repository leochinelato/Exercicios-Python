def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f"ERRO! '{n}' não é um número")
    return n


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
