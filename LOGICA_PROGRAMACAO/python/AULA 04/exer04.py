# Exercício 04
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota 0 a 100 para ser aprovado será acima de 70 e menor que 50 esse valor será reprovado porém vamos acrescentar uma nova condição que entre 50 e 70 recuperação.

print("Bem-Vindo a Média de Notas!")
print("Iniciando...")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))
média = (nota1+nota2) /2

if nota1 >=70:
    print("O resultado de sua conta é?", média)
    print("Aprovado")
elif nota2 <=50:
    print("Reprovado")