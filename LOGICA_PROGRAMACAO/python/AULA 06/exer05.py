# Exercício 5 - 
# Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

# Exemplo 1
peso = input("Digite o valor do peso")

for temp in medidas:
    if temp == 50:
        print(f"{temp} está no peso ideal")
    elif temp > 50:
        print(f"{temp} está acima de peso ideial")

    elif temp < 50:
        print(f"{temp} está abaixo do peso ideal")
    else:
        print("Encerrar")