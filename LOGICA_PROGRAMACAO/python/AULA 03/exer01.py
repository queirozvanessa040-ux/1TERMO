# Exercício 01
# Cáculo de notas por semestre onde terá duas notas formativas e uma nota somativa para enecerrar o semestre.
# Lembrete: os valores de notas são 0 a 100, exibir o resultado do ano e incluir nota de média do primeiro e segundo semestre
print("Primeiro semestre")
form01 = int(input("Valor da nota formativa: \n"))
form02 = int(input("Valor da nota formativa: \n"))
som01 = int(input("Valor da nota somativa: \n"))
total = (form01 + form02 + som01) / 3
print(f"A média de seu semestre foi: \n", round(total,1))
print("Segundo semestre")
form03 = int(input("Valor da nota formativa: \n"))
form04 = int(input("Valor da nota formativa: \n"))
som02 = int(input("Valor da nota somativa: \n"))
total01 = (form03 + form04 + som02) / 3
print(f"A média de seu semestre foi: \n", round(total01,1))
ano = (total + total01) / 2
print(f"A média final das suas notas do ano foram: \n", round(ano,1))