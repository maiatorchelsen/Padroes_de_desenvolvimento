# Python já possui o padrão Iterator embutido na própria linguagem através
#  dos métodos mágicos
#  __iter__ e __next__.
#  Se implementarmos esses métodos, podemos usar o loop for nativo do Python,
#  mantendo o encapsulamento!

# Interface Iterator


class PlaylistPythonIterator:

    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self._position >= len(self._collection):
            raise StopIteration

        musica = self._collection[self._position]
        self._position += 1

        return musica

# Coleção


class PlaylistPythonica:

    def __init__(self):
        self._musicas = []

    def add_musica(self, musica):
        self._musicas.append(musica)

    def __iter__(self):
        return PlaylistPythonIterator(self._musicas)

# Cliente


playlist = PlaylistPythonica()

playlist.add_musica("Song A")
playlist.add_musica("Song B")
playlist.add_musica("Song C")

print("--- Iterator Pythonico ---")

for musica in playlist:
    print(f"Tocando: {musica}")