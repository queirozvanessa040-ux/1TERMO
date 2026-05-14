## Aula: Gestão de Projetos e Engenharia de Requisitos em Sistemas Operacionais
## 1. Concepção e Levantamento de Requisitos

* Brainstorming: Técnica em grupo para definir novos recursos do SO (ex: melhorias no sistema de arquivos ou segurança).
* Entrevistas: Reuniões estruturadas com administradores e usuários para levantar dores de desempenho (ex: lentidão na troca de contexto).

------------------------------
## 2. Engenharia de Requisitos no Contexto de SO

* Requisitos Funcionais: Funções que o sistema executa (ex: gerenciar alocação de RAM, isolar processos, executar chamadas de sistema).
* Requisitos Não Funcionais: Atributos de qualidade (ex: tempo de boot inferior a 10s, conformidade com padrão POSIX, criptografia AES-256).

------------------------------
## 3. Modelagem, Documentação e Validação

* Diagramas: Modelos visuais para mapear comportamentos complexos (ex: Diagrama de Transição de Estados de um Processo).
* Relatórios Técnicos: Documentos formais detalhando a arquitetura interna do kernel, consumo de memória e benchmarks de hardware.
* Prototipagem: Desenvolvimento de modelos iniciais (ex: simulação de algoritmo de escalonamento em Python antes da implementação final em C).

------------------------------
## 4. Gestão Ágil de Desenvolvimento (Scrum & Kanban)## Framework Scrum (Foco em Iteração e Ritmo)

* Baseia-se em ciclos de tempo fixos chamados Sprints (geralmente de 1 a 4 semanas).
* Product Backlog: Lista priorizada de funcionalidades pendentes (ex: criar driver de vídeo, corrigir bug de concorrência).
* Daily Scrum: Reunião diária de 15 minutos para alinhar o progresso do desenvolvimento e remover impedimentos de código.

## Método Kanban (Foco em Fluxo e Visualização)

* Utiliza um quadro visual para acompanhar a evolução das tarefas em tempo real.
* Limita o Trabalho em Progresso (WIP - Work in Progress) para evitar gargalos na equipe.

+--------------------+--------------------+--------------------+

|    A Fazer (To Do) |  Em Progresso (WIP)|  Concluído (Done)  |
+--------------------+--------------------+--------------------+

| [ ] Corrigir Swap  | [ ] Otimizar CPU   | [X] Atualizar Kernel|
| [ ] Atualizar Docs |                    |                    |
+--------------------+--------------------+--------------------+

------------------------------
## 5. Prática em Aula: Mapeamento de Fluxo

   1. Atividade: Dividir a turma em grupos (Scrum Teams) e criar um quadro Kanban para gerenciar a correção de falhas em um módulo simulado do SO.

------------------------------
Para personalizar o encerramento deste material, informe:

* Os alunos utilizarão alguma ferramenta de software (como Trello, Jira ou Miro) para gerenciar o Kanban?
* Você deseja incluir um exemplo detalhado de Diagrama (ex: o ciclo de vida de um processo em formato de texto/tabela)?
* Qual o tempo total disponível para a realização da atividade prática em grupo?


