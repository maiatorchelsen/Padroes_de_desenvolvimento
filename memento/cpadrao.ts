// 1. O MEMENTO: Objeto imutável
// Usamos "readonly" para garantir que, uma vez criado, não seja alterado.
class MementoPedido {
    constructor(
        public readonly descricao: string, 
        public readonly preco: number
    ) {}
}

// 2. O ORIGINATOR: A classe dona do estado
class PedidoCafe {
    // Propriedades privadas, inacessíveis por fora da classe
    private descricao: string;
    private preco: number;

    constructor(descricao: string, preco: number) {
        this.descricao = descricao;
        this.preco = preco;
    }

    public adicionarIngrediente(ingrediente: string, valor: number): void {
        this.descricao += `, + ${ingrediente}`;
        this.preco += valor;
    }

    // Tira a "foto" do estado
    public salvar(): MementoPedido {
        return new MementoPedido(this.descricao, this.preco);
    }

    // Restaura a partir de uma "foto"
    public restaurar(memento: MementoPedido | null): void {
        if (memento !== null) {
            this.descricao = memento.descricao;
            this.preco = memento.preco;
        }
    }

    public mostrarPedido(): void {
        console.log(`Pedido atual: ${this.descricao} | Preço Total: R$${this.preco.toFixed(2)}`);
    }
}

// 3. O CARETAKER: O Zelador do histórico
class HistoricoPedidos {
    private historico: MementoPedido[] = [];

    public push(memento: MementoPedido): void {
        this.historico.push(memento);
    }

    public pop(): MementoPedido | null {
        // Retorna o último item ou null se estiver vazio
        return this.historico.pop() || null;
    }
}

// Simulação da execução principal
function executarComMemento() {
    console.log("--- CAFETERIA COM PADRÃO MEMENTO ---");

    const pedido = new PedidoCafe("Café Espresso Base", 5.00);
    const zelador = new HistoricoPedidos();
    
    pedido.mostrarPedido();

    // Salva o estado inicial
    zelador.push(pedido.salvar());

    console.log("\nAdicionando Leite...");
    pedido.adicionarIngrediente("Leite", 2.00);
    pedido.mostrarPedido();

    // Salva o estado antes do caramelo
    zelador.push(pedido.salvar());

    console.log("\nAdicionando Caramelo...");
    pedido.adicionarIngrediente("Caramelo", 1.50);
    pedido.mostrarPedido();

    // Desfazendo (Remover Caramelo)
    console.log("\n[Desfazer] Cliente mudou de ideia sobre o Caramelo...");
    pedido.restaurar(zelador.pop());
    pedido.mostrarPedido();

    // Desfazendo (Remover Leite)
    console.log("\n[Desfazer] Cliente mudou de ideia sobre o Leite...");
    pedido.restaurar(zelador.pop());
    pedido.mostrarPedido();
}

executarComMemento();