# 1. O Laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 01
for lote in range (1, 6):
    print(f"Processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

# Continuação do Exemplo 01
for carros in range(10):
    print(f"Quantidade de carros {carros}")

# Exemplo 02
# Contar até 4
for i in range(5):
    print(i)

# Exemplo 03
pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
maquinas = ["Máquina 1", "Máquina 2"]

for item in pecas:
    print(f"Item em estoque: {item}")
    for maq in maquinas:
        print(f"Máquinas que temos {maq}")

# 2. Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

# Repete enquanto a temperatura estiver segura
# Início
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    temperatura += 3 # Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Interação
opcao = ""
# lower() = minúsculo
# upper() = maiúsculo

while opcao != "sair":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
    if opcao != "sair":
        print(f"Dado '{opcao}' registrado no banco de dados.")
print("Sistema encerrado.")