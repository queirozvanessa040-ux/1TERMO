# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# Exemplo 1
for i in range(1, 6):
    consumo = float(input("Digite o consumo"))
    total = consumo + i
    print(f"O valor de consumo é {total}")

# Exemplo 2
total = 0
for i in range(1, 6):
    consumo = float(input(f"Digite o consumo da {i} máquina "))
    total += consumo
    print(f"Consumo total da fábrica {total}")