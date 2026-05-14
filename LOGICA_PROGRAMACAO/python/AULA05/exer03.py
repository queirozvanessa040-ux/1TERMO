# Exercício 03
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("Tabuada")
num = int(input("Digite o valor"))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")