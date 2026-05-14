# Exercício 04

print("Inspeção de Peças")
nota1 = float(input("Digite a nota de inspeção 1 (0 a 10)..."))
nota2 = float(input("Digite a nota de inspeção 2 (0 a 10)...")) 
nota3 = float(input("Digite a nota de inspeção 3 (0 a 10)..."))
media = (nota1 + nota2 + nota3) / 3
print(f"Média de qualidade da peça: {media:.2f}")
print("Média de qualidade da peça: ", round(media,2))