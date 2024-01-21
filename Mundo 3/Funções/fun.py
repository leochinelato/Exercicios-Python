def dobra(lst):
    """
    -> Recebe uma lista de valores e dobra todos eles.
    :param lst: Lista de valores que será dobrada.
    :return: sem retorno
    """
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 8, 7, 5, 4]
dobra(valores)
print(valores)

help(dobra)
