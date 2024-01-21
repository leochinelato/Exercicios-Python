def titulo(msg):
    print("-" * 40)
    print(msg.center(40))
    print("-" * 40)


def menu(lista):
    titulo("MENU PRINCIPAL")
    for pos, item in enumerate(lista):
        print(f"\033[32m{pos+1}\033[m - \033[33m{item}\033[m")
    print("-" * 40)
    opc = leiaInt("Escolha: ")
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Opção incorreta.")
            continue
        else:
            return n
