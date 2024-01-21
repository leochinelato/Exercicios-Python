# Ler vários números inteiros
# Parar quando user digitar 999
# Dizer quantos números foram digitados
# Soma entre eles

n = q = s = 0

while True:
    print("="*38)
    n = int(input("Digite um número (999 para sair): "))
    if n == 999:
        break
    s += n
    q += 1

print(f"A quantidade de números digitados foi de {q} \nA soma entre eles foi de {s}")
