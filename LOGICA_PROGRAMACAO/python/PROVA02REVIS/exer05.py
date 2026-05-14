# Exercício 05

print("Termostato Inteligente")
temperatura = float(input("Digite a temperatura do motor em C°..."))
if temperatura < 40:
    print("Baixa carga")
elif 40 <= temperatura <= 70:
    print("Normal")
else:
    print("ALERTA: Resfriamento Ativado!")

# OU

print("Termostato Inteligente - Versão 2")
temperatura = float(input("Digite a temperatura do motor em C°..."))
if temperatura < 40:
    print("Baixa carga")
elif temperatura <= 70:
    print("ALERTA: Resfriamento Ativado!")
else:
    print("Normal")