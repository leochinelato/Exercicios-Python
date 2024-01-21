#perguntar a quantidade de KM percorridos:
kmPercorridos = float(input("Qual a quantidade de KM percorridos pelo carro alugado? "))

#perguntar por quantos dias ele foi alugado
diasAlugado = int(input("Por quantos dias o carro ficou alugado? "))

#calcular o preço a pagar, sendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
precoCarro = (60*diasAlugado) + (0.15 * kmPercorridos)

print("O preço total deu: {:.2f}".format(precoCarro))