# Princípios SOLID - Guia Rápido

Este projeto demonstra a aplicação dos cinco princípios básicos do Design Orientado a Objetos (SOLID).

SOLID é um acrônimo mnemônico que representa um conjunto de diretrizes de design de software que ajudam a criar sistemas mais **manuteníveis**, **flexíveis** e **escaláveis**.

| Princípio | Acrônimo | Explicação Simples | O que o código aprende? |
| :--- | :--- | :--- | :--- |
| **Responsabilidade Única** | **S**RP | Uma classe deve ter apenas **uma** razão para mudar. | Separa a lógica de negócio da persistência de dados. |
| **Aberto/Fechado** | **O**CP | Uma classe deve ser aberta para **extensão**, mas fechada para **modificação**. | Adicionar um novo recurso não exige mudar o código existente, apenas criar um novo. |
| **Substituição de Liskov** | **L**SP | Subtipos (classes filhas) devem ser totalmente **substituíveis** pelos seus tipos base. | Garantir que a herança não quebre o comportamento esperado pelo código cliente. |
| **Segregação de Interfaces** | **I**SP | Clientes não devem ser forçados a depender de interfaces (contratos) que não utilizam. | Interfaces "gordas" (com muitos métodos) devem ser divididas em interfaces menores e específicas. |
| **Inversão de Dependência** | **D**IP | Módulos de alto nível não devem depender de módulos de baixo nível, mas sim de **abstrações** (interfaces). | Depender de contratos (`ABC`) em vez de classes concretas, permitindo a Injeção de Dependência. |

## Como os Exemplos didáticos em Python Demonstramdo SOLID

No código dessa pasta, usamos os seguintes recursos para aplicar os princípios:

* **SRP (Responsabilidade Única):** Ações como calcular (`CalculadoraSalario`) e salvar (`FuncionarioRepositorio`) são separadas em classes distintas.
* **OCP (Aberto/Fechado):** Usamos a classe base abstrata (`TipoFrete`) e herança para permitir a adição de novos tipos de frete sem modificar a classe principal (`CalculadoraFrete`).
* **LSP (Substituição de Liskov):** As classes herdeiras (`Quadrado`, `Retangulo`) satisfazem o contrato da classe base (`Forma`), garantindo que a função cliente possa usar qualquer subtipo sem erros.
* **ISP (Segregação de Interfaces):** Usamos múltiplas classes abstratas (`Impressora`, `Scanner`) para criar contratos pequenos e específicos, evitando que classes simples implementem métodos desnecessários.
* **DIP (Inversão de Dependência):** O módulo de alto nível (`ServicoNotificacao`) recebe a dependência (`MensagemSender`) via construtor (Injeção de Dependência), dependendo apenas da abstração, e não da implementação concreta (`EmailSender` ou `SmsSender`).
