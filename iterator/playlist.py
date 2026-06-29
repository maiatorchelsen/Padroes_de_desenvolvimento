# Sem iterator, o cliente precisa conhecer a estrutura interna da Playlist 
# (uma lista) e como percorrê-la (usando índices).

class Playlist:
    def __init__(self):
        self.musicas = []

    def add_musica(self, musica):
        self.musicas.append(musica)


# Cliente
playlist = Playlist()
playlist.add_musica("Song A")
playlist.add_musica("Song B")
playlist.add_musica("Song C")

print("--- Sem Iterator ---")

for i in range(len(playlist.musicas)):
    print(f"Tocando: {playlist.musicas[i]}")

# Problemas
# O cliente sabe que existe uma lista.
# O cliente sabe usar índices.
# se a lista virar um set, o código quebra.
# Alto acoplamento.