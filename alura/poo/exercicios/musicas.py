class Musica:
    musicas = []

    def __init__(self, nome="", artista="", duracao=int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")


musica1 = Musica(nome="Vida chique", artista="Veigh", duracao=180)


Musica.listar_musicas()
