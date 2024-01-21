valores = []

opcao = "s"

while opcao in "Ss":
    valor = int(input("Digite um valor: "))
    
    if valor in valores:
        print("Valor duplicado! Não vou adicionar...")
    else:
        valores.append(valor)
        print("Valor adicionado com sucesso... ")

    opcao = str(input("Quer continuar? [S/N]: "))

valores.sort()
print("="*40)
print("Valores digitados: ")
print(valores)
print("="*40)