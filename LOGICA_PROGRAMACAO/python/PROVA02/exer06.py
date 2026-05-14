# Exercício 06

print("A = ALIMENTOS")
print("E = ELETRÔNICOS")
print("Não reconhecido")
produto = (input("Insira o código do produto: "))

if produto == "A":
    print(f"ALIMENTO")
elif produto == "2":
    print(f"ELETRÔNICOS")
else:
    print(f"Não reconhecido")