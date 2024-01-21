opcao = "s"
valores = []

while opcao in "sS":
    valores.append(int(input("Digite um valor: ")))
    opcao = str(input("Deseja continuar? [S/N]: ")).strip()

print("=-"*30)
print(f"{len(valores)} números foram digitados")
print("="*30)
print("A lista ordenada de forma decrescente: ")
valores.sort(reverse=True)
print(valores)
print("="*30)
if 5 in valores:
    print("O número 5 está na lista!")
else:
    print("O número 5 NÃO está na lista. :(")