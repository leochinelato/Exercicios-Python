# Programa que le uma frase em mostre:
# Quantas vezes aparece a letra "A".
# Em que posição aparece o primeiro A.
# Em que posição aparece o ultimo A.

frase = str(input("Digite uma frase: ")).upper().strip()

print("A frase acima possui {} letras A".format( frase.count('A') ))

print("A primeira letra A aparece na posição {}".format( frase.find("A") +1 ))
print("A última letra A aparece na posição {}".format( frase.rfind("A") +1 ))