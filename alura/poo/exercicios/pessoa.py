class Pessoa:
    def __init__(self, nome="", idade=int, profissao=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.profissao} "

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Olá {self.nome}, cargo {self.profissao}"


pessoa_1 = Pessoa("Leonardo", 21, "Analista de Sistemas")

pessoa_1.aniversario()
print(pessoa_1)
print(pessoa_1.saudacao)
