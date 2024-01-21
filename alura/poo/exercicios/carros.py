class Carros:
    def __init__(self, modelo="", cor="", ano=int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano}"


carro_1 = Carros("Tucson", "Preto", 2014)

print(carro_1)
