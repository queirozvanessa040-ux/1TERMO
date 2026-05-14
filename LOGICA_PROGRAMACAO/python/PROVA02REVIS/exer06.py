# Exercício 06

print("Classificador de Lotes!")
codigo_produto = input("Digite o código de produto...")
if codigo_produto == "A":
    print("Alimentos")
elif codigo_produto == "E":
    print("Eletrônicos")
else:
    print("Desconhecido")

# OU

print("Classificador de Lotes!")
codigo_produto = input("Digite o código de produto...")
if codigo_produto.startswith("A"):
    print("Alimentos")
elif codigo_produto.startswith("E"):
    print("Eletrônicos")
else:
    print("Desconhecido")