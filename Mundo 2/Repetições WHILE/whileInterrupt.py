n = s = q = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    q += 1

print(f"Você digitou {q} números e a soma deles é {s}")
