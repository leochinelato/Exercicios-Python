frase = str(input("Digite uma frase: ")).strip()
palindromo = frase[::-1]

if frase.replace(" ", "").lower() == palindromo.replace(" ", "").lower():
    print(f"A frase {frase} é um Palíndromo")
else:
    print(f"A frase {frase} não é um palíndromo")
