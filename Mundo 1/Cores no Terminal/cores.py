#1
print("\033[7;37mOlá, mundo!")

#2
print("\033[33;44m Olá \033[m mundo!")

#3
nome = "Leonardo"
print("Olá, prazer em te conhecer, {}{}{}".format("\033[4m",nome, "\033[m"))

#4
cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "amarelo": "\033[33m"}

print("Olá, prazer em te conhecer {}{}{} !!!".format( cores["amarelo"], nome, cores["limpa"] ))