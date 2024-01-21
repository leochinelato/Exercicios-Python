def notas(*nums, sit=False):
    """
    -> Relatório das notas da sala de aula.
    :nums: Lista com todas as notas.
    :sit: Situação dos alunos conforme média 6

    """
    todasNotas = dict()

    todasNotas["Quantidade de notas"] = len(nums)
    todasNotas["Maior Nota"] = max(nums)
    todasNotas["Menor Nota"] = min(nums)
    todasNotas["Média da turma"] = sum(nums) / len(nums)
    if sit:
        if todasNotas["Média da turma"] >= 6:
            todasNotas["Situação"] = "MÉDIA OK"
        else:
            todasNotas["Situação"] = "MÉDIA RUIM"
    return todasNotas


resp = notas(5, 9, 7, 6, sit=True)
print(resp)
