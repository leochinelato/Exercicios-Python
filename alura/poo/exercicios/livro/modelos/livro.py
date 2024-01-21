class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self.ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f"{self._titulo} | {self._autor} | {self.ano_publicacao}"
    
    def emprestar(self):
        self._disponivel = not self._disponivel
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livro if livro.ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis