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