// A classe do pedido expõe suas propriedades publicamente
class PedidoCafeSemMemento {
    public descricao: string;
    public preco: number;

    constructor(descricao: string, preco: number) {
        this.descricao = descricao;
        this.preco = preco;
    }

    public adicionarIngrediente(ingrediente: string, valor: number): void {
        this.descricao += `, + ${ingrediente}`;
        this.preco += valor;
    }

    public mostrarPedido(): void {
        console.log(`Pedido atual: ${this.descricao} | Preço Total: R$${this.preco.toFixed(2)}`);
    }
}

// Simulação da execução principal
function executarSemMemento() {
    console.log("--- CAFETERIA SEM PADRÃO MEMENTO ---");

    const pedido = new PedidoCafeSemMemento("Café Espresso Base", 5.00);
    pedido.mostrarPedido();

    // Arrays atuando como pilhas (Stacks) para salvar o histórico
    const historicoDescricoes: string[] = [];
    const historicoPrecos: number[] = [];

    // 1. Salvar estado atual antes de alterar
    historicoDescricoes.push(pedido.descricao);
    historicoPrecos.push(pedido.preco);

    console.log("\nAdicionando Leite...");
    pedido.adicionarIngrediente("Leite", 2.00);
    pedido.mostrarPedido();

    // 2. Salvar estado atual antes de alterar novamente
    historicoDescricoes.push(pedido.descricao);
    historicoPrecos.push(pedido.preco);

    console.log("\nAdicionando Caramelo...");
    pedido.adicionarIngrediente("Caramelo", 1.50);
    pedido.mostrarPedido();

    // Desfazer a última ação (Remover Caramelo)
    console.log("\n[Desfazer] Cliente mudou de ideia sobre o Caramelo...");
    if (historicoDescricoes.length > 0 && historicoPrecos.length > 0) {
        pedido.descricao = historicoDescricoes.pop()!;
        pedido.preco = historicoPrecos.pop()!;
    }
    pedido.mostrarPedido();

    // Desfazer mais uma vez (Remover Leite)
    console.log("\n[Desfazer] Cliente mudou de ideia sobre o Leite...");
    if (historicoDescricoes.length > 0 && historicoPrecos.length > 0) {
        pedido.descricao = historicoDescricoes.pop()!;
        pedido.preco = historicoPrecos.pop()!;
    }
    pedido.mostrarPedido();
}

executarSemMemento();