# Exercício 02
# Escreva um programa que solicite ao usuário uma lista de palavra e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValoueError: se o usuário digitar um valor que não seja uma string.

try:
    palavras = input("Digite uma lista de palavras separadas por espaço...").split()
    contagem = {}
    for palavra in palavras:
     num_palavras = palavras.count(f" ") + 1
     print(palavras)
     if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
        print("Contagem de palavras:")
    for palavra, contagem in contagem.items():
      print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")