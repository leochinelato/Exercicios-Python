def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Tipo de dado digitado não é inteiro.")
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Tipo de dado digitado não é real.")
            continue
        else:
            return n


n = leiaInt("Digite um número inteiro: ")
n2 = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {n} e real {n2}")
