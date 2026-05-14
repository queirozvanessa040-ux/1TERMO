# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças:
# Medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]

for temp in medidas:
    if temp > 50:
        print(f"{temp}Aprovada!!")
    elif temp < 50:
        print(f"{temp} Reprovado")
    else:
        print("Encerrar")