from abc import ABC, abstractmethod


# Interface Iterator
class Iterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# Iterator Concreto
class PlaylistIterator(Iterator):

    def __init__(self, musicas):
        self._musicas = musicas
        self._posicao = 0

    def has_next(self):
        return self._posicao < len(self._musicas)

    def next(self):
        musica = self._musicas[self._posicao]
        self._posicao += 1
        return musica


# Coleção
class Playlist:

    def __init__(self):
        self._musicas = []

    def add_musica(self, musica):
        self._musicas.append(musica)

    def create_iterator(self):
        return PlaylistIterator(self._musicas)


# Cliente
playlist = Playlist()

playlist.add_musica("Song A")
playlist.add_musica("Song B")
playlist.add_musica("Song C")

iterator = playlist.create_iterator()

print("--- Iterator Clássico ---")

while iterator.has_next():
    print(f"Tocando: {iterator.next()}")

# Vantagens

# ✅ Cliente não conhece a estrutura interna.

# ✅ Podemos trocar lista por set ou banco de dados.

# ✅ Baixo acoplamento.