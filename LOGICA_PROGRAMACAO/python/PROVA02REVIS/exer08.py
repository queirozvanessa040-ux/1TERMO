# Exercício 08

print("Cálculo de Descarte")
total_pecas = int(input("Digite o total de peças produzidas..."))
total_defeituosas = int(input("Digite o total de peças defeituosas..."))
descarte_percentual = (total_defeituosas / total_pecas) * 100
if descarte_percentual > 5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")
print(f"Descarte percentual: {descarte_percentual:.2f}%")