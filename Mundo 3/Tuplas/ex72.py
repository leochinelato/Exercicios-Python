# Tupla do 0 ao 20 escritos em extenso
# O programa deverá ler um número pelo teclado e mostrá-lo por extenso

extenso = "zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"



while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        break
    print("Número errado...")

print(f"Você digitou o número {extenso[numero]}")