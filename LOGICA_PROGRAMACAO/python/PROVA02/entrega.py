# Exercício 01

nome = input("Digite o nome do operador: ")
turno = input("Digite o turno (A, B ou C): ")
print(f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

# Exercício 02

hora1 = float(input("Qual a quantidade de peças em 1hr? "))
hora8 = float(input("Qual a quantidade de peças em 8hr"))
total = hora1 + hora8

print("A quantidade peças produzidas em 1 hora são: ", hora1)
print("A quantidade de peças produzidas em 8 horas são: ", hora8)
print("O total de peças produzidas são: ", total)

# Exercício 03

print("Bem-vindo ao Bar!")
bar = float(input("Digite a pressão em Bar: "))
psi = bar * 14.5
print(f"{bar} Bar equivalem a {psi:.2f} PSI.")

# Exercício 04
total0 = 3
not1 = float(input("Digite a sua primeira nota: "))
not2 = float(input("Digite a sua segunda nota: "))
not3 = float(input("Digite a sua terceira nota: "))
total = (not1 + not2 + not3) / total0

print("A qualidade das peças ao serem inspecionadas são:", total)

# Exercício 05

print("Bem-vindo ao Termostato Inteligente!")
temperatura = float(input("Digite a temperatura do motor (°C): "))

if temperatura < 40:
    print("Status: Baixa carga")
elif 40 <= temperatura <= 70:
    print("Status: Normal")
else:
    print("ALERTA: Resfriamento Ativado!")

# Exercício 06

print("A = ALIMENTOS")
print("E = ELETRÔNICOS")
print("Não reconhecido")
produto = (input("Insira o código do produto: "))

if produto == "A":
    print(f"ALIMENTO")
elif produto == "2":
    print(f"ELETRÔNICOS")
else:
    print(f"Não reconhecido")

# Exercício 07

# Coletando os dados do usuário
sensor_porta = input("A porta está aberta ou fechada? ")
botao_emergencia = input("O botão de emergência está ligado ou desligado? ")

# Verificando as condições de segurança
if sensor_porta == "fechada" and botao_emergencia == "desligado":
    print("Segurança confirmada: A máquina pode ser ligada.")
elif sensor_porta != "fechada":
    print("Atenção: A porta precisa estar fechada para operar.")
elif botao_emergencia != "desligado":
    print("Atenção: Desative o botão de emergência primeiro.")
else:
    print("Erro no sistema: Verifique os sensores.")

# Exercício 08

pecas_produzidas = float(input("Digite a quantidade de peças produzidas"))
pecas_defeituosas = float(input("Digite a quantidade de peças defeituosas"))
taxa_descarte = pecas_defeituosas * 0.05

if  pecas_defeituosas > taxa_descarte:
    print(f"Revisar Processo")

# Exercício 09

medida = float(input("Digite o valor da medida da peça em mm: "))
limite_inferior = 9.8
limite_superior = 10.2

if medida >= 9.8 and medida <= 10.2:
    print(f"A medida {medida}mm está DENTRO da tolerância")
elif medida < 9.8:
    print(f"A medida {medida}mm está ABAIXO da tolerância.")
else:
    print(f"A medida {medida}mm está ACIMA da tolerância.")

# Exercício 10

for i in range (10, 0, -1):
    print(f"{i} Prensa Ativida!") 

# Exercício 11

peso_total = 0

while True:
    
        peso = float(input("Digite o peso da caixa (ou 0 para encerrar): "))
        if peso == 0:
            break
        peso_total += peso
        print(f"O peso total acumulado é: {peso_total}")

# Exercício 12

maior_temp = 0

for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i}: "))
    
    if temp > maior_temp:
        maior_temp = temp
    maior_temp += temp
print(f"A maior temperatura lida foi: {maior_temp}")