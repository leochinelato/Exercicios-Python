from modelos.avaliacao import Avaliacao


class Eletronico:
    """Representa um eletronico e características
    Returns:
        _type_: _description_
    """

    eletronicos = []

    def __init__(self, nome, categoria):
        """Inicia uma instância de academia.

        Parametros:
            - nome (str): Nome do eletronico.
            - categoria (str): Categoria do eletrônico.
        """
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Eletronico.eletronicos.append(self)

    def __str__(self):
        """Retorna em string o eletronico."""
        return f"[{self._nome}]]"

    @classmethod
    def listar_eletronicos(cls):
        """Mostra uma lista formatada com todos os eletronicos e suas características"""

        print(
            "{:<12} | {:<12} | {:<12} | {:<12}".format(
                "Eletronico", "Categoria", "Avaliação", "Status"
            )
        )
        for eletronico in Eletronico.eletronicos:
            print(
                f"{eletronico._nome:<12} | {eletronico._categoria:<12} | {eletronico.media_avaliacoes:<12} | {eletronico.ativo:<12}"
            )

    @property
    def ativo(self):
        """Transforma o nosso True ou False em um emoji."""
        return "✔︎" if self._ativo else "𐄂"

    def alternar_estado(self):
        """Alterna eletronico entre Ativo/Inativo"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o eletronico.

        Args:
            cliente (str): O nome do cliente que fez avaliação.
            nota (float): A nota que o cliente deu.
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Faz o calculo da media das avaliações e retorna"""
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantia_notas = len(self._avaliacao)
        media = round(soma_notas / quantia_notas, 1)
        return f"{media} ☆"
