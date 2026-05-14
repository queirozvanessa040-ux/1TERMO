# Exercício 11

peso_total = 0

while True:
    
        peso = float(input("Digite o peso da caixa (ou 0 para encerrar): "))
        if peso == 0:
            break
        peso_total += peso
        print(f"O peso total acumulado é: {peso_total}")

