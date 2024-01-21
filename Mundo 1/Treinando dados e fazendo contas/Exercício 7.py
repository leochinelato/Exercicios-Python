aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do {}: ".format(aluno)))
nota2 = float(input("Digite a segunda nota do {}: ".format(aluno)))

media = (nota1 + nota2) / 2

print("A média do {} é igual a {:.2f}".format(aluno,media))