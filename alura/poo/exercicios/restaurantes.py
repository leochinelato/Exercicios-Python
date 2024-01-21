class Restaurante:
    def __init__(self, nome="", categoria="", ativo=False, avaliacao=int, aberto=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.aberto = aberto

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo} | {self.avaliacao} | {self.aberto} "


restaurante_1 = Restaurante("Madero", "Fast Food", True, 5, True)

print(restaurante_1)
