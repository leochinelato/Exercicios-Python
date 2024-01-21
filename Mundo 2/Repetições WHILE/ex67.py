# Mostre a tabuada de vários números, um de cada vez.
# O usuário precisará digitar o número da tabuada que ele quer.
# Programa interrompido quando o número for negativo.

while True:
    n = int(input("Digite um número: "))
    if n < 0:
        print("=" * 25)
        print("PROGRAMA INTERROMPIDO...")
        print("=" * 25)
        break
    for c in range(1, 10 + 1):
        print(f"{n} x {c:2} = {n*c}")
