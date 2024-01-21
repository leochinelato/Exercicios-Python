from modelos.livro import Livro

livro_1 = Livro("Mais esperto que o diabo", "Napoleon Hill", 2011)
livro_2 = Livro("As armas da persuasão", "Robert B. Cialdini", 2012)

Livro.livros = [livro_2,livro_2]


def main():
    print(livro_1)
    print(livro_2)


if __name__ == "__main__":
    main()
