# Exercício 01
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota base de 50 é aprovado e menor que esse valor será reprovado

print("Bem-Vindo a Média Calculadora!")
print("Iniciando...")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))
média = (nota1+nota2) /2

if nota1 >=50:
    print("O resultado de sua conta é?", média)
    print("Aprovado")
else:
    print("Reprovado")

    print("sapatos-Você contém 10% de desconto.")