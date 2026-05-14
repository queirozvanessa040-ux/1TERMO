## Aula: Lógica de Programação com Python, Java, JavaScript e Controle de Versão com GitHub
## 1. Fundamentos da Lógica de Programação

* Algoritmos: Sequências de passos finitos para resolver problemas do mundo real.
* Variáveis: Espaços nomeados na memória para armazenar dados do sistema.
* Operadores: Símbolos lógicos, relacionais e aritméticos para manipulação de dados.

------------------------------
## 2. Estruturas de Controle nas Linguagens de Programação## Condicionais (if/else)
A tomada de decisão baseada em condições lógicas estruturada em cada ecossistema:
## Python

idade = 18if idade >= 18:
    print("Maior de idade")else:
    print("Menor de idade")

## Java / JavaScript

int idade = 18; // Em JS, use 'let idade = 18;'if (idade >= 18) {
    System.out.println("Maior de idade"); // Em JS, use 'console.log()'
} else {
    System.out.println("Menor de idade");
}

## Repetição (while / for)
Execução de blocos de códigos repetidas vezes enquanto a condição for verdadeira:
## Python

for i in range(3):
    print(f"Contagem: {i}")

## Java / JavaScript

for (int i = 0; i < 3; i++) { // Em JS, use 'for (let i = 0; i < 3; i++)'
    System.out.println("Contagem: " + i); // Em JS, use 'console.log()'
}

------------------------------
## 3. Características das Linguagens Escolhidas

* Python: Sintaxe limpa, tipagem dinâmica, focado em legibilidade e análise de dados.
* JavaScript: Linguagem nativa da web, tipagem dinâmica, focada em interatividade.
* Java: Linguagem robusta, fortemente tipada, compilada, focada em orientação a objetos.

------------------------------
## 4. Hospedagem de Código e Versionamento com GitHub

* Git vs GitHub: Git é a ferramenta local; GitHub é a plataforma em nuvem.
* Repositório: Pasta virtual onde o projeto e o histórico de alterações ficam salvos.
* Fluxo de Trabalho Básico:

git init               # Inicializa o Git na pasta local do projeto
git add .              # Prepara os arquivos modificados para o salvamento
git commit -m "Commit" # Grava a foto atual do código com uma mensagem
git push origin main   # Envia os arquivos locais para o servidor do GitHub

------------------------------
## 5. Prática Proposta: Desafio Multi-Linguagem

   1. Passo 1: Criar um script que filtre números pares em uma lista (em Python, Java ou JavaScript).
   2. Passo 2: Criar um repositório público no perfil pessoal do GitHub.
   3. Passo 3: Subir o arquivo do script criado usando os comandos do terminal Git.


