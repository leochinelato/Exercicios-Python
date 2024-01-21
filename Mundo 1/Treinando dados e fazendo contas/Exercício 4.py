dado = input("Escreva algo: ")

print("O tipo primitivo da variável é: ", type(dado))
print("É numérico? ",dado.isnumeric())
print("É alfabetico? ",dado.isalpha())
print("Só tem maíusculas? ", dado.isupper())
print("Só tem minúsculas? ", dado.islower())