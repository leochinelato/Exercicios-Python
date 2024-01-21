try:
    a = int(input("Digite um valor: "))
    b = int(input("Digite outro valor: "))
    c = a / b
except ZeroDivisionError:
    print(f"Não é possível dividir um número por 0 (zero)")
except (ValueError, TypeError):
    print(f"Não é possível dividir esses valores digitados.")
except KeyboardInterrupt:
    print("O usuário não quis informar os números.")
finally:
    print("Volte sempre!")