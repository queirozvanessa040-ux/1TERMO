## Aula: Sistemas Operacionais – Windows vs. Linux
## 1. Introdução e Arquitetura dos Sistemas

* Kernel Monolítico (Linux): Todos os serviços do sistema rodam no mesmo espaço de memória do núcleo.
* Kernel Híbrido (Windows): Combina a velocidade do monolítico com a modularidade do microkernel.
* Espaço do Usuário vs. Espaço do Kernel: Mecanismos de proteção para isolar aplicações de funções críticas.

------------------------------
## 2. Gerenciamento de Processos e Threads## Windows

* Uso do Gerenciador de Tarefas e Process Explorer para monitoramento visual.
* Abstração baseada em objetos (Processos possuem um ou mais Threads de execução).
* Comandos essenciais via PowerShell:

Get-Process                  # Lista processos ativos
Stop-Process -Name "notepad" # Encerra um processo específico

## Linux

* Tudo é tratado como arquivo; processos são listados no diretório /proc.
* Árvore de processos hierárquica iniciada pelo processo systemd (PID 1).
* Comandos essenciais via Terminal:

ps aux                       # Lista todos os processos do sistema
top                          # Monitora o uso de CPU e memória em tempo real
kill -9 1234                 # Encerra o processo de ID 1234 de forma forçada

------------------------------
## 3. Gerenciamento de Memória e Sistemas de Arquivos

* Memória Virtual: Uso de paginação para expandir a RAM física (pagefile.sys no Windows / Partição ou arquivo Swap no Linux).
* Sistemas de Arquivos:
* NTFS (Windows): Suporte a permissões avançadas, criptografia nativa (BitLocker) e journaling.
   * EXT4 (Linux): Estrutura baseada em Inodes, alta eficiência de alocação e journaling robusto.

------------------------------
## 4. Prática em Aula: Comparativo de Comandos Básicos

| Operação | Prompt/PowerShell (Windows) | Terminal (Linux) |
|---|---|---|
| Listar arquivos | dir / Get-ChildItem | ls -la |
| Criar diretório | mkdir / New-Item | mkdir |
| Ver configurações de rede | ipconfig | ip a ou ifconfig |
| Verificar rotas de rede | tracert | traceroute |

------------------------------
## 5. Atividade Proposta: Análise de Desempenho

   1. Atividade Windows: Abrir o Monitor de Recursos, identificar o consumo de memória de paginação e simular o encerramento de um processo travado via PowerShell.
   2. Atividade Linux: Acessar uma máquina virtual via terminal, analisar a carga do sistema com o comando uptime e identificar gargalos com o comando free -m.

------------------------------
Para adaptar este material ao laboratório disponível na sua instituição, informe:

* A prática será feita utilizando Máquinas Virtuais (como VirtualBox) ou os computadores possuem Dual Boot?
* Qual distribuição Linux (Ubuntu, Debian, Fedora, etc.) será utilizada na aula?
* Você deseja focar mais na Interface Gráfica (GUI) ou na Linha de Comando (CLI) para a avaliação dos alunos?


