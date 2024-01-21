class Cliente:
    def __init__(self, nome="", email="", telefone=int, ativo=True):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.ativo = ativo

    def __str__(self):
        return f"{self.nome} | {self.email} | {self.telefone} | {self.ativo}"


cliente_1 = Cliente("José", "jose@gmail.com", 984497096)

print(cliente_1)
