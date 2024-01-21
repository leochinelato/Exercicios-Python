#cores

cores = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'

}

# Programa que pega usuário e senha, o usuário precisa ter mais de 18 anos.

print('='*35)
usuario = str(input('Digite o seu nome: ')).strip()
print('='*35)
idade = int(input('Digite a sua idade: '))
print('='*35)

if idade >= 18:
    print('{}Você pode acessar o nosso sistema!{}'.format(cores['verde'],cores['limpa']))

    print('='*40)
    print("Seja bem vindo ao urubu do pix!")
    print("Selecione um dos valores abaixo:")
    print("(1) Deposite R$50 e retorne R$200")
    print("(2) Deposite R$200 e retorne R$800 + Bônus de R$100")
    print("(3) Deposite R$500 e retorne R$2000 + Bônus de R$1000")

    escolha = int(input("Digite a opção escolhida: "))

    if escolha == 1:
        print("Você escolheu a opção 1, deposite R$ 50 na chave pix: x")
        check = input("Assim que efetuar o depósito, digite OK: ")

        if check.lower() == "ok":
            print("Parabéns, você será recompensado em até 24 horas!!")

    elif escolha == 2:
        print("Você escolheu a opção 2, deposite R$ 200 na chave pix: x")
        check = input("Assim que efetuar o depósito, digite OK: ").strip()
        
        if check.lower() == "ok":
            print("Parabéns, você será recompensado em até 24 horas!!")

    elif escolha == 3:
        print("Você escolheu a opção 3, deposite R$ 500 na chave pix: x")
        check = input("Assim que efetuar o depósito, digite OK: ")
        
        if check.lower() == "ok":
            print("Parabéns, você será recompensado em até 24 horas!!")
        

else:
    print('{}Infelizmente não poderá acessar o nosso sistema'.format(cores['vermelho']))