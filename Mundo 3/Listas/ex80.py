valores = []

# digitar 5 valores
# na hora que o usuario digitar precisamos saber onde o numero vai ficar, fazendo com que a nossa lista sempre esteja em ordem crescente.

# adicionar elementos no final: valores.append(valor)
# adicionar valores em outras posiçÕes: valores.insert(pos, valor)

# Usuário digita 5 valores, serão adicionados numa lista...
# Porém, cada valor que o usuário digitar será comparado com o valor anterior, sendo maior, será um append, sendo menor, sera comparado com o anterior até achar um que ele é maior, assim, será insertado antes do maior.

valores = []

for c in range(0, 5):
    n = int(input("Digite o valor: "))

    if c == 0 or n > valores[-1]:
        valores.append(n)
        print("O valor foi inserido na última posição.")
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f"O valor foi inserido na posição {pos}")
                break
            pos += 1

print("="*40)
print(f"A lista é: {valores}")