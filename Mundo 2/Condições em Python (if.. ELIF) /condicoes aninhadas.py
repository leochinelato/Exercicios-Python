# se            if
# senão se      elif
# senão         else

nome = str(input("Qual o seu nome? ")).strip()
idade = int(input("Qual a sua idade? "))

if idade < 18:
    print("Menor de idade, não pode acessar!")
elif idade >= 60:
    print("Você já é idoso, não pode acessar.")
else:
    print("Você pode acessar!")

# Pessoas com 18 ou acima e abaixo de 60 podem acessar, fora isso, não podem.