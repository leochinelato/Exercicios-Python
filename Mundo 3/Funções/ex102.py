def fatorial(num=1, show=False):
    """
    -> Calcula fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O fatorial do valor num.
    """
    f=1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


teste = fatorial(5, True)
print(teste)
