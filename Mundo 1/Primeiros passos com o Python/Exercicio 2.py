print("="*40)
n1 = int(input("Digite um número: "))
print("="*40)
n2 = int(input("Digite outro número: "))
print("="*40)

soma = n1 + n2

print("A {}soma{} entre {}{}{} e {}{}{} é igual a {}{}{}".format("\033[32m","\033[m","\033[4m",n1,"\033[m", "\033[4m", n2,"\033[m", "\033[4m",soma,"\033[m"))
print("="*40)