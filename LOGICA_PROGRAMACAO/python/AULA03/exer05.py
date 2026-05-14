# Exercício 05
# Criar um algortimo para calcular a venda de livros e que toda venda apresente um desconto fixo de 5%

print("Bem-Vindo a Bibliio!")
valor = float(input("Digite o valor dos livros: \n"))
quantidade = float(input("Digite a quantidade de livros: \n"))
total = valor * quantidade
print("O valor da compra destes livros são?", total)
desconto = float(input("Digite o valor do desconto:"))
ltotal = total - desconto
print("O valor da compra destes livros com o desconto é?", ltotal)