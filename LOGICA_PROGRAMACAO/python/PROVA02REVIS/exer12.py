# Exercício 12

print("Múltiplas Leituras")
temperaturas = [] # Insirir as informações que você digitou. 
for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i} em °C..."))
    temperaturas.append(temp)

print(f"Maior temperatura lida: {max(temperaturas):.2f} °C")
print(f"Menor temperatura lida: {min(temperaturas):.2f} °C")

# max = maior/máximo
# min = menor
# sum = somar as informações/valores
# .append = significa trazer as informações/valores e formar uma lista