# Exemplo 01
for i in range (1, 11):
    print(f"\nTabuada do {i}:")
    for j in range (1, 11):
        print(f"{i} x {j} = {i * j}")

# Exemplo 02
# Lista de temperaturas lidas pelo sensor por minuto
leituras = [70, 75, 82, 98, 110, 85, 80]

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
        break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligado. Aguardando manutenção.")

materiais = ["metal", "metal", "plastico", "metal", "vidro", "argila", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue # Pula o restante do código abaixo e vai para a próxima peça

# Este código só roda se a peça for de metal
print(f"Processando peça de {peca}. Furando e polindo...")

print("Fim do lote de produção.")

# Este código só roda se a peça for de metal
print(f"Processando peça de {peca}. Furando e polindo...")

print("Fim do lote de produção.")