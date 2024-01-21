from datetime import date
def voto(anoNasc):
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 16:
        return "Voto Negado"
    elif 16 <= idade < 18 or idade > 65:
        return "Voto Opcional"
    else:
        return "Voto Obrigatório"
    
    
ano = int(input("Em que ano nasceu? "))
print(voto(ano))