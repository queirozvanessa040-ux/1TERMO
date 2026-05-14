# Exercício 05

print("Bem-vindo ao Termostato Inteligente!")
temperatura = float(input("Digite a temperatura do motor (°C): "))

if temperatura < 40:
    print("Status: Baixa carga")
elif 40 <= temperatura <= 70:
    print("Status: Normal")
else:
    print("ALERTA: Resfriamento Ativado!")
