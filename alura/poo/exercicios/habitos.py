class Habito:
    habitos = []

    def __init__(self, nome, frequencia):
        self.nome = nome
        self.frequencia = frequencia
        self.ativo = False
        Habito.habitos.append(self)

    def __str__(self):
        return f"[{self.nome}] | [{self.frequencia}]"

    def listar_habitos():
        for habito in Habito.habitos:
            print(
                f"Nome: {habito.nome} | Frequencia: {habito.frequencia} | Ativo: {habito.ativo} "
            )


habito_treinar = Habito("Treinar", 6)

Habito.listar_habitos()

@property
def ativo(self):
    return "☒" if self.ativo else "☐"