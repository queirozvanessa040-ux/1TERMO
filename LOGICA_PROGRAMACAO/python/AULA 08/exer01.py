# Exercício 01:
# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.

quantidade = 0
lista = 6


try:
    quantidade = int(input("Quantos números você deseja inserir "))
    for i in range(quantidade):
            num = int(input(f"Digite o número {i+1}: "))
    media = lista * num
    print(f"A lista inserida foi: {lista}")
    print(f"A média dos números é: {media:.2f}")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
