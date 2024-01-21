from modelos.avaliacao import Avaliacao


class Academia:
    """Representa uma academia e características
    Returns:
        _type_: _description_
    """

    academias = []

    def __init__(self, nome):
        """Inicia uma instância de academia.

        Parametros:
            - nome (str): Nome da academia.
        """
        self._nome = nome.title()
        self._ativo = False
        self._avaliacao = []
        Academia.academias.append(self)

    def __str__(self):
        """Retorna em string a academia."""
        return f"[{self._nome}]]"

    @classmethod
    def listar_academias(cls):
        """Mostra uma lista formatada com todas as academias e suas características"""

        print("{:<12} | {:<12} | {:<12}".format("Academia", "Avaliação", "Status"))
        for academia in Academia.academias:
            print(
                f"{academia._nome:<12} | {academia.media_avaliacoes:<12} | {academia.ativo:<12}"
            )

    @property
    def ativo(self):
        """Transforma o nosso True ou False em um emoji."""
        return "✅" if self._ativo else "❌"

    def alternar_estado(self):
        """Alterna academia entre Ativo/Inativo"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para academia.

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
