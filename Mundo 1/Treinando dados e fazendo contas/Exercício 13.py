funcionario = input("Digite o nome do funcionário: ")

#ler o salário atual do funcionário
salarioInicial = float(input("Digite o salário do funcionário {}: R$".format(funcionario)))

#faça uma conta somando 15% no salario inicial
salarioFinal = salarioInicial + (salarioInicial*15/100)

#imprima o salário com aumento e 15%
print("O salário atual do colaborador {}, com aumento de 15% é de: R${}".format(funcionario,salarioFinal))