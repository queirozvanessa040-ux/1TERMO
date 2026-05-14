# Exercício 1
# 1. Contador de Produção (for)
# Uma esteira processa 10 peçaspor ciclo. Crie um programa que use for para contar de 1 a 10, para cada número, imprima: "Peça n° X processada com sucesso". No final, exiba "Ciclo de produção concluído".

print("Produção")
for X in range(10):
    print(X)
    print("Peça n° X processada com sucesso")
    print("Ciclo de produção concluído")
print("Produção do dia finalizado!")

# OU

for ciclo in range(1, 10):
    print(f"Processando ciclos de peças {ciclo}...+")
    print(f"Peça n° {ciclo}. Processada com sucesso")
    print("Ciclo de produção concluído")