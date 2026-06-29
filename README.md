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
