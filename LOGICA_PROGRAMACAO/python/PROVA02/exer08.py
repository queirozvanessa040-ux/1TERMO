# Exercício 08

pecas_produzidas = float(input("Digite a quantidade de peças produzidas"))
pecas_defeituosas = float(input("Digite a quantidade de peças defeituosas"))
taxa_descarte = pecas_defeituosas * 0.05

if  pecas_defeituosas > taxa_descarte:
    print(f"Revisar Processo")
    