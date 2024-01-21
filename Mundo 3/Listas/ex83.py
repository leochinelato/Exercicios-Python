parAberto = []
parFechado = []

expressao = str(input("Digite a expressão: "))

for e in expressao:
    if e in "(":
        parAberto.append(e)
    if e in ")":
        parFechado.append(e)

if len(parAberto) == len(parFechado):
    print("Sua expressão está correta!")
else:
    print("Expressão errada...")