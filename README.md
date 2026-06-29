# Padrões de Desenvolvimento

Estudar padrões de projeto, entender o seu funcionamento e aplicação e traçar um comparativo entre eles.

# Iterator

# Strategy

Aluno: Brian da Silva Guterres

🎯 Objetivo
Este repositório contém o trabalho prático sobre Padrões de Projeto (Design Patterns) do GoF. O objetivo é estudar, aplicar e analisar o padrão Strategy, apresentando soluções de código com e sem a aplicação do padrão para fins didáticos.

📚 Padrão Escolhido: Strategy
Para este trabalho, o foco foi na categoria de Padrões Comportamentais. O padrão escolhido para estudo e implementação foi o Strategy.

🔍 Detalhamento do Padrão
📌 Propósito
O Strategy é um padrão de projeto comportamental que permite definir uma família de algoritmos, colocar cada um deles em classes separadas e fazer com que os objetos dessas classes sejam intercambiáveis. Ele permite que o algoritmo varie independentemente dos clientes que o utilizam.

🚨 Problema (Código Sem o Padrão)
Imagine um sistema de e-commerce que precisa calcular o valor do frete. Inicialmente, a loja oferece apenas entrega via PAC. Depois, adiciona Sedex e, em seguida, uma Transportadora Privada.

No código sem o padrão, teríamos uma única classe Pedido com um método calcularFrete() contendo uma estrutura gigantesca de if/else ou switch/case.

Por que isso é ruim?
Fere o Princípio de Aberto/Fechado (OCP) do SOLID: toda vez que uma nova modalidade de frete for adicionada, a classe principal precisará ser modificada.
O código se torna difícil de ler, manter e testar, pois a classe de contexto (o Pedido) fica inchada com as regras de negócio de todos os tipos de frete.

💡 Solução (Código Com o Padrão)

- O padrão Strategy sugere que você extraia todas essas regras de cálculo de frete para classes separadas (chamadas de Estratégias).

- Criamos uma interface comum chamada EstrategiaFrete com um método calcular().

- Criamos classes concretas para cada tipo de frete que implementam essa interface (FretePac, FreteSedex, FreteTransportadora).

- A classe Pedido (o Contexto) agora guarda apenas uma referência para a interface EstrategiaFrete. Ela não sabe como o frete é calculado, apenas delega a tarefa chamando o método calcular() da estratégia que foi configurada.

- Por que isso é bom?
  Agora, se quisermos adicionar entrega via "Motoboy", deve-se criar uma nova classe FreteMotoboy que implementa a interface. Assim, a classe Pedido permanece intocada.

⚖️ Pontos Fortes e Fracos
Prós:

- Troca em tempo de execução: Você pode alterar o comportamento (o algoritmo de frete) de um objeto durante a execução do programa.
- Isolamento de complexidade: Isola os detalhes de implementação de um algoritmo do código que o utiliza.
- Composição sobre Herança: Substitui a herança por composição, tornando o sistema mais flexível.
- Open/Closed Principle (OCP): Você pode introduzir novas estratégias sem precisar alterar o código do contexto original.

Contras:

- Complexidade adicional: Se você tem apenas um ou dois algoritmos que raramente mudam, não há motivo para inflar o projeto com novas interfaces e classes.
- Conhecimento das estratégias: O cliente (quem chama o código) geralmente precisa estar ciente das diferenças entre as estratégias para poder selecionar a mais adequada.
- Limitações de linguagens modernas: Algumas linguagens modernas suportam funções de primeira classe, permitindo implementar comportamentos semelhantes de forma mais simples (passando funções anônimas) sem precisar criar dezenas de classes extras.

📝 Conclusão
A aplicação do padrão Strategy demonstrou ser extremamente valiosa para sistemas onde múltiplas variações de um mesmo comportamento são necessárias. Embora introduza uma complexidade estrutural inicial (maior quantidade de arquivos e interfaces), o ganho em manutenibilidade e escalabilidade compensa rapidamente. O código se torna muito mais limpo, modularizado e fácil de ser coberto por testes unitários, provando na prática os benefícios dos princípios SOLID na engenharia de software.

📚 Fontes
https://refactoring.guru/pt-br/design-patterns/strategy
Refactoring Guru - Design Pattern: Strategy
Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John; Design Patterns: Elements of Reusable Object-Oriented Software. (GoF). 1994.

# Memento

Aluno: Eduardo Maia

# Estudo de Caso: Padrão de Projeto Memento (Lembrança) em TypeScript

Este repositório foi criado para demonstrar de forma prática a aplicação do padrão de projeto comportamental **Memento** em uma aplicação TypeScript. O cenário escolhido é o sistema de customização de pedidos de uma cafeteria, onde o cliente pode adicionar ingredientes e precisa de uma funcionalidade de "Desfazer" (*Undo*) caso mude de ideia.

O projeto contém duas implementações distintas para fins comparativos:
1. **Sem o Padrão Memento**: Uma solução ingênua que resolve o problema, mas viola os princípios de encapsulamento e gera alto acoplamento.
2. **Com o Padrão Memento**: Uma solução arquitetada que isola as responsabilidades e protege o estado do objeto principal.

---

## ☕ O Cenário do Problema

Imagine um totem de autoatendimento em uma cafeteria. O cliente inicia o pedido com um café base (ex: Espresso, R$ 5,00) e começa a customizá-lo adicionando itens extras, como Leite (R$ 2,00) e Caramelo (R$ 1,50). 

A aplicação precisa oferecer um botão **"Desfazer"**. Se o cliente decidir que não quer mais o Caramelo, o sistema deve remover o ingrediente do texto descritivo e subtrair o valor exato do preço total, retornando o pedido ao estado imediatamente anterior.

---

## ❌ 1. Abordagem Sem o Padrão Memento

Na primeira abordagem, a funcionalidade de "Desfazer" é implementada delegando o controle do histórico diretamente para a função principal do sistema.

### Como o código funciona por trás dos panos:
* **Classe `PedidoCafeSemMemento`**: Atua apenas como um repositório de dados estruturado com propriedades públicas (`descricao` e `preco`). Qualquer classe externa tem permissão para ler e alterar esses valores através de comandos como `pedido.preco = ...`.
* **Gerenciamento do Histórico**: Na execução principal, criamos dois arrays nativos do TypeScript atuando como pilhas (`string[]` e `number[]`). Toda vez que um ingrediente vai ser adicionado, o código cliente faz um "print" manual do estado atual, fazendo um `.push()` da descrição e do preço nos arrays.
* **Ação de Desfazer**: Quando o cliente desfaz a ação, o programa faz um `.pop()` nos arrays para extrair os últimos valores salvos e sobrescreve as propriedades públicas do `PedidoCafeSemMemento`.

### Por que esta abordagem é prejudicial? (Problemas de Arquitetura)
1. **Quebra de Encapsulamento:** A classe perde o controle sobre as suas próprias regras de negócio. O estado interno do objeto é exposto para o mundo exterior.
2. **Alto Acoplamento:** O código cliente precisa saber exatamente como a classe do pedido é composta internamente (quais são os tipos de dados e os nomes das propriedades).
3. **Dificuldade de Manutenção:** Se amanhã o café precisar armazenar novas informações (como tabela nutricional, peso ou tempo de preparo), você será obrigado a criar novos arrays no código cliente e alterar toda a lógica externa de salvamento.

---

## 🚀 2. Abordagem Com o Padrão Memento

Para corrigir as falhas de arquitetura, aplicamos a estrutura formal descrita pelo padrão Memento. A responsabilidade de capturar e restaurar o estado é devolvida para quem realmente é dono dele, dividindo o sistema em três papéis essenciais:

### 📑 Os Três Pilares do Padrão no Código

#### A. O Memento (`MementoPedido`)
É um objeto de valor puro cuja única utilidade é armazenar um instantâneo (*snapshot*) do estado do pedido em um determinado momento.
* **Imutabilidade:** Suas propriedades (`descricao` e `preco`) possuem o modificador `readonly`. Uma vez instanciado pelo construtor, o Memento nunca mais pode ser alterado por ninguém. Ele funciona como uma "caixa preta" selada.

#### B. O Originator / Originador (`PedidoCafe`)
É a classe que possui o estado real que queremos proteger e salvar.
* **Encapsulamento Estrito:** Repare que as variáveis de estado (`descricao` e `preco`) agora são estritamente privadas (`private`). Nenhuma classe de fora consegue modificá-las diretamente.
* **Método `salvar()`:** Quando invocado, o próprio pedido cria uma instância de `MementoPedido`, passando uma cópia dos seus dados privados para o construtor do memento e retornando-o.
* **Método `restaurar(memento: MementoPedido)`:** O pedido recebe um memento (a caixa preta), lê os dados imutáveis contidos nele e atualiza suas próprias variáveis privadas.

#### C. O Caretaker / Zelador (`HistoricoPedidos`)
É o responsável exclusivo por guardar e organizar os mementos ao longo do tempo.
* **Isolamento:** Ele armazena uma lista interna (um array `MementoPedido[]`). O Zelador sabe como empilhar um novo estado (`push`) e como extrair o último (`pop`).
* **Regra de Ouro:** O Zelador **nunca** lê e **nunca** altera o conteúdo que está dentro do Memento. Para ele, o memento é apenas um objeto opaco que precisa ser guardado.

---

## 🔄 Fluxo de Execução com Memento

1. O objeto `PedidoCafe` é criado com o seu estado inicial.
2. Antes de adicionar um ingrediente, o cliente executa: `zelador.push(pedido.salvar())`. O pedido gera o snapshot e o zelador o guarda.
3. O ingrediente é adicionado via método interno `pedido.adicionarIngrediente(...)`.
4. Caso o usuário decida desfazer, o sistema executa: `pedido.restaurar(zelador.pop())`. O zelador entrega o último memento salvo e o pedido se auto-restaura de forma segura.

---

## 📊 Tabela Comparativa

| Critério de Análise | Sem o Padrão Memento | Com o Padrão Memento |
| :--- | :--- | :--- |
| **Encapsulamento** | **Ruim.** O estado interno é exposto publicamente para que o histórico funcione. | **Excelente.** O estado permanece estritamente privado (`private`). |
| **Princípio de Responsabilidade Única (SRP)** | **Violado.** O código cliente gerencia as regras de negócio e a lógica de histórico simultaneamente. | **Respeitado.** O Originador cuida do negócio, o Zelador cuida do histórico, o Memento armazena. |
| **Acoplamento** | **Alto.** Se a estrutura interna do pedido mudar, toda a lógica de histórico externa quebra. | **Baixo.** O histórico externo manipula apenas a classe abstrata/fechada do Memento. |
| **Escalabilidade** | **Difícil.** Adicionar novos atributos ao pedido exige a criação de novos arrays/pilhas manuais. | **Fácil.** Novos atributos exigem alteração apenas nas classes internas do padrão. |

---

## 🛠️ Como Executar os Exemplos

1. Certifique-se de ter o [Node.js](https://nodejs.org/) instalado em sua máquina.
2. É recomendado instalar o `ts-node` e o `typescript` globalmente para rodar os arquivos diretamente:
   ```bash
   npm install -g typescript ts-node