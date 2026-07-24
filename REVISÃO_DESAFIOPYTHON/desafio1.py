#Desafio 1: Condicionais e Operações (O Aluguel de Carro)
#Enunciado em Python: Escreva um programa em Python que receba o número
#de dias que um carro foi alugado e a quantidade de Km rodados.
#  - O aluguel custa R$ 90,00 por dia.
#  - Se o cliente rodou até 100 km no total, paga R$ 0,20 por Km rodado.
#  - Se rodou mais de 100 km, paga R$ 0,15 por Km rodado.
#Exiba o valor total a pagar formatado com duas casas decimais.
#  - O que avalia no aluno: Variáveis, conversão de tipos (float/int), condicionais
#    (if/else) e cálculos matemáticos.

print("Bem-Vindo ao Aluguel de Carros!")
print("Ao alugar um automóvel o valor a ser pago será R$ 90.00 por dia! Além de cada 100 Km rodado é equivalado R$ 0,20")
print("Com estás informações em mente deseja alugá-lo?")

dias = int(input("Dias alugados: "))
km = float(input("Km rodados: "))

preco_dias = dias * 90

if km <= 100:
    preco_dias = km * 0.20
else:
    preco_km = km * 0.15

total = preco_dias + preco_km
print(f"Total a pagar: R$ {total:.2f}")