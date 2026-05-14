# Exercício 12

maior_temp = 0

for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i}: "))
    
    if temp > maior_temp:
        maior_temp = temp
    maior_temp += temp
print(f"A maior temperatura lida foi: {maior_temp}")