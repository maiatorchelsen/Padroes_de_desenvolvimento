
## Cenário 1: Sem o Padrão Iterator
Nesta abordagem, o código cliente precisa conhecer exatamente como a coleção armazena os dados 
(neste caso, um array interno) para conseguir interagir com ela. Se mudarmos o array para um Set
 ou uma Linked List no futuro, o cliente quebra.

 // Sem_Iterator.ts

class Playlist {
  // O cliente PRECISA saber que os dados estão em um array público
  public musicas: string[] = [];

  addMusica(musica: string): void {
    this.musicas.push(musica);
  }
}

## Código Cliente
const minhaPlaylist = new Playlist();
minhaPlaylist.addMusica("Song A");
minhaPlaylist.addMusica("Song B");
minhaPlaylist.addMusica("Song C");

## Problema: O cliente está acoplado à estrutura interna (array)
console.log("--- Percorrendo SEM Iterator ---");
for (let i = 0; i < minhaPlaylist.musicas.length; i++) {
  console.log(`Tocando: ${minhaPlaylist.musicas[i]}`);
}
//
`Se quisermos mudar a estrutura interna para um Set, o código cliente quebra completamente`
// minhaPlaylist.musicas = new Set<string>(); // Isso causaria um erro no código cliente

//-------------------------------------------------------------
## Cenário 2: Com o Padrão Iterator
Nesta abordagem, a classe Playlist implementa o padrão Iterator, permitindo que o cliente percorra 
as músicas sem precisar conhecer a estrutura interna. O cliente pode usar um iterador para acessar as músicas,

// Com_Iterator.ts

// 1. Interface do Iterador
interface MyIterator<T> {
  next(): T | null;
  hasNext(): boolean;
}

// 2. Interface da Coleção Agregada
interface Container<T> {
  createIterator(): MyIterator<T>;
}

// 3. Iterador Concreto para a Playlist
class PlaylistIterator implements MyIterator<string> {
  private collection: string[];
  private position: number = 0;

  constructor(collection: string[]) {
    this.collection = collection;
  }

  public next(): string | null {
    if (this.hasNext()) {
      return this.collection[this.position++];
    }
    return null;
  }

  public hasNext(): boolean {
    return this.position < this.collection.length;
  }
}

// 4. Coleção Concreta
class PlaylistComIterator implements Container<string> {
  // A estrutura de dados agora é PRIVADA. Ninguém de fora sabe que é um array.
  private musicas: string[] = [];

  public addMusica(musica: string): void {
    this.musicas.push(musica);
  }

  // Fábrica que cria o iterador correto para esta classe
  public createIterator(): MyIterator<string> {
    return new PlaylistIterator(this.musicas);
  }
}

// --- Código Cliente ---
const playlistAgrupada = new PlaylistComIterator();
playlistAgrupada.addMusica("Song A");
playlistAgrupada.addMusica("Song B");
playlistAgrupada.addMusica("Song C");

## O cliente não sabe (e não se importa) como as músicas estão guardadas por baixo dos panos
const iterator = playlistAgrupada.createIterator();

console.log("--- Percorrendo COM Iterator ---");
while (iterator.hasNext()) {
  console.log(`Tocando: ${iterator.next()}`);
}