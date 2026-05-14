# Exercício 03
# Criar um algoritmo para aplicação de descontos para produtos como sapatos aplicar 10%, roupas 5% e perfumes 2%

print("Bem-Vindo a Loja1")
print("1 = sapatos-Você contém 10% de desconto!")
print("2 = roupas-Você contém 5% de desconto!")
print("3 = perfumes-Você contém 2% de desconto")
produtos = int(input("Digite o produto que deseja"))
# valor = int(input("Digite o valor do produto \n"))
# quantidade = int(input("Digite a quantidade de produtos: \n"))
# desconto = int(input("Digite o valor do desconto \n"))
# compra1 = (valor*quantidade) - desconto

if produtos == 1:
    valor = int(input("Digite o valor do produto \n"))
    quantidade = int(input("Digite a quantidade de produtos: \n"))
    desconto = int(input("Digite o valor do desconto \n"))
    compra1 = (valor*quantidade) - desconto
    print("O resultado de sua conta foi:", compra1)
elif produtos == 2:
    valor = int(input("Digite o valor do produto \n"))
    quantidade = int(input("Digite a quantidade de produtos: \n"))
    desconto = int(input("Digite o valor do desconto \n"))
    compra1 = (valor*quantidade) - desconto
    print("O resultado de sua conta foi:", compra1)
elif produtos == 3:
    valor = int(input("Digite o valor do produto \n"))
    quantidade = int(input("Digite a quantidade de produtos: \n"))
    desconto = int(input("Digite o valor do desconto \n"))
    compra1 = (valor*quantidade) - desconto
    print("O resultado de sua conta foi:", compra1)
else:
    ("Agradecemos pela sua vinda! Volte Sempre!")