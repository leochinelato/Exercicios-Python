# Programa que le o nome completo da pessoa e mostre em seguida o primeiro e o ultimo nome separadamente.

nome = str(input("Digite o seu nome completo: ")).strip()

nomeSeparado = nome.split()

print("O seu primeiro nome é: {}".format( nomeSeparado[0] ))
print("O seu último nome é: {}".format( nomeSeparado[-1] ))