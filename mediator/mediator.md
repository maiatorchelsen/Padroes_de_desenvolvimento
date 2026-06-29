# Padrão de Projeto - Mediator (GoF)
Este repositório apresenta o estudo e a implementação do padrão comportamental Mediator, demonstrando sua importância na redução do acoplamento e na organização da comunicação entre múltiplos componentes ou serviços de um sistema.

# 🧭 O que é o Mediator?
O Mediator é um padrão de projeto comportamental que permite reduzir as dependências caóticas entre objetos. Ele restringe as comunicações diretas entre os componentes de um sistema e os força a colaborar apenas através de um objeto mediador central, promovendo um design mais limpo e modular.

# Problema
Imagine que a sua equipe desenvolveu um sistema backend para o gerenciamento de convidados de um evento. O sistema conta com diversos serviços especializados: um serviço de convidados (GuestService), um serviço de auditoria (LogService), um serviço de notificações (EmailService) e um painel de estatísticas (DashboardService).

Surgiu a necessidade de que, sempre que um novo convidado for registrado e tiver seu status definido como confirmado (booleano), o sistema deve registrar um log, enviar um e-mail de boas-vindas e atualizar o dashboard em tempo real. A abordagem inicial seria fazer o GuestService instanciar e chamar os métodos de todos esses outros serviços diretamente. Contudo, esta solução traz sérios problemas:

* Alto Acoplamento: A classe de convidados, que deveria cuidar apenas da lógica de persistência e validação da entidade, passa a conhecer detalhes de infraestrutura de e-mail e logs.

* Dificuldade de Reutilização: Se você quiser reutilizar o LogService ou o EmailService em outra parte do sistema, será difícil isolá-los, pois eles formaram uma "teia de aranha" de dependências com outras classes.

* Falta de Extensibilidade: Se na semana seguinte for necessário adicionar o envio de um SMS de confirmação, será obrigatório modificar novamente a classe principal de convidados, aumentando o risco de quebrar regras de negócio já consolidadas.

# Solução
O padrão Mediator resolve este dilema sugerindo que você extraia toda a comunicação direta entre as classes para um objeto independente chamado mediador. Os objetos param de conversar diretamente entre si e passam a se comunicar apenas com o mediador.

No nosso cenário, o GuestService não precisa mais saber que o EmailService ou o LogService existem. Quando um convidado é adicionado, o serviço de convidados apenas notifica o mediador dizendo: "Um convidado foi criado com sucesso".

O mediador, que atua como uma torre de controle, recebe essa notificação, identifica quais outros serviços precisam agir (como disparar o e-mail e registrar o log) e faz as chamadas necessárias. Dessa forma, os componentes do sistema (chamados de colegas) tornam-se totalmente independentes uns dos outros, conhecendo apenas a interface do mediador.

# 🧱 Estrutura do Padrão
O padrão é composto pelos seguintes elementos principais:

Mediator (Interface): Declara métodos de comunicação com os componentes, geralmente um método único de notificação onde os componentes podem passar o contexto do evento.

Concrete Mediator: Encapsula as relações entre os vários componentes. Ele mantém referências a todos os componentes que gerencia e orquestra a lógica de quem deve ser chamado quando um evento ocorre.

Component / Colleague (Classe Base): Declara a referência para o mediador. As classes de componentes não conhecem as outras, apenas a interface do mediador.

Concrete Component: Implementa a lógica de negócio específica. Quando precisa se comunicar com outro componente, ele não o chama diretamente, mas sim notifica o seu mediador.

# 📌 Prós e contras
✅ Princípio de Responsabilidade Única: Permite extrair a lógica de comunicação e orquestração entre diversos componentes para um único local (o mediador), tornando o código mais fácil de manter.

✅ Princípio Aberto/Fechado: Facilita a introdução de novos mediadores para orquestrar os componentes de maneiras diferentes sem alterar o código dos componentes originais.

✅ Desacoplamento: Reduz drasticamente o acoplamento entre as classes do sistema, permitindo que cada serviço ou componente seja testado e reutilizado de forma isolada.

❌ O Problema do Objeto Deus (God Object): Se não for bem desenhado, com o crescimento da aplicação, o mediador pode centralizar tanta lógica de controle que se transforma em um objeto gigante e onisciente, tornando-se um gargalo de manutenção.

# Padrões relacionados
Observer: O Mediator e o Observer são frequentemente usados em conjunto ou como alternativas. Enquanto o Observer distribui a comunicação dinamicamente (publish/subscribe) sem um controlador central estrito, o Mediator centraliza o fluxo de comunicação de forma mais rígida e explícita.

Facade: Semelhante ao Mediator por simplificar o uso de subsistemas complexos, mas com uma diferença crucial: o Facade cria uma interface unidirecional (o cliente chama o Facade, mas os subsistemas não conhecem o Facade), enquanto o Mediator atua bidirecionalmente (os componentes conhecem e notificam o Mediator).

# Conclusões sobre o Mediator
O padrão Mediator demonstra ser uma arquitetura fundamental para o desenvolvimento backend quando a comunicação ponto-a-ponto entre classes se torna uma rede complexa e insustentável. Ele transfere a responsabilidade da coreografia do sistema para um maestro central, garantindo que regras de negócio permaneçam isoladas e limpas. Embora exija vigilância contínua para evitar que a classe mediadora se torne um monolito que sabe demais, o Mediator é a escolha ideal para orquestrar fluxos de trabalho complexos, emissão de eventos e sistemas onde a independência dos componentes é uma prioridade.

Fontes
https://refactoring.guru/pt-br/design-patterns/mediator

Livro GoF - Design Patterns: Elements of Reusable Object-Oriented Software

Livro Código Limpo (Clean Code) - Robert C. Martin

Autoria: Samuel Silva da Costa Vargas