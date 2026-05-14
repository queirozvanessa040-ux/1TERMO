# Exercício 02
# Imagine a produção de frutos em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi

print("Feira de frutos")
frutas = ["Bananas"]

for item in frutas:
    print(f"Item em estoque: {item}")
    for frutas in range(1, 11):
        print(f"Quantidade de bananas {frutas}")
print("Total de Bananas finalizado")

frutas1 =["Mangas"]
for item1 in frutas1:
    print(f"Item em estoque: {item1}")
    for frutas1 in range(1, 6):
        print(f"Quantidade de mangas {frutas1}")
print("Total de Mangas finalizado")

frutas2 = ["Melancia"]
for item2 in frutas2:
    print(f"Item em estoque: {item2}")
    for frutas2 in range(1, 11):
        print(f"Quantidade de melancia {frutas2}")
print("Total de Melancias finalizado")

frutas3 = ["Abacaxi"]
for item3 in frutas3:
    print(f"Item em estoque: {item3}")
    for frutas3 in range(1, 14):
        print(f"Quantidade de abacaxi {frutas3}")
print("Total de Abacaxis finalizado")

num1 = 10
num2 = 5
num3 = 10
num4 = 13
resultado_soma = num1 + num2 + num3 + num4
print("A quantidade de todas as frutas é?", resultado_soma)
