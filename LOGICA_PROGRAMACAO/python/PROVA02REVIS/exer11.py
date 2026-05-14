# Exercício 11

print("Soma de Produção (Acumulador)")
peso_total = 0
while True:
    peso_caixa = float(input("Digite o peso da caixa (0 para parar)..."))
    if peso_caixa == 0:
        break
    peso_total += peso_caixa
    print(f"Peso total acumulado: {peso_total:.2f} kg")