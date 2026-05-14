# Conteúdo sobre lógica
# Exemplo 01
print("Expressões lógicas ")
idade = int(input("Digite sua idade"))

if idade >=18:
    print("Você é maior de idade.")
    print("Pode tirar carteira de motorista.")
elif idade >=16:
    print("Você ainda não é maior de idade, mas já pode votar.")
else:
    print("Você é menor de idade.")

# if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usado para múltiplas condições).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).

# Exemplo 02
print("Escolha sua modalidade?")
print("Opção 1: TI")
print("Opção 2: Humanas")
print("Opção 1: Exatas")
modalidade = int(input("Digite sua opção de modalidade por números"))
if modalidade == 1:
    print("Você escolheu TI")
elif modalidade == 2:
    print("Você escolheu Humanas")
else:
    print("Você escolheu Exatas")

# Ao colocar == é como se disesse "É realmente aquela opção"

# Exemplo 03
print("Categoria de Séries e Filmes.")
print("Escolha uma categoria")
print("Séries = S")
print("Filmes = F")
categoria = input("Digite sua categoria")
if categoria == "S":
    print("Sua escolha foi para Séries")
elif categoria == "F":
    print("Sua escolha foi para Filmes")
else:
    print("Você não escolheu nenhuma opção")
    print("Terminamos nossa sessão.")

# Exemplo 04
print("Calculadora como condições")
print("Escolha como quer calcular")
print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")
calculadora = float(input("Digite sua opção para calcular \n"))
if calculadora == 1:
    print("1 = Você escolheu soma")
    soma1 = int(input("Digite o primeiro valor \n"))
    soma2 = int(input("Digite o segundo valor \n"))
    print(soma1+soma2)
    print("O resultado de sua conta é?", soma1+soma2)
elif calculadora == 2:
    print("2 = Você escolheu subtração")
    subtração1 = int(input("Digite o primeiro valor \n"))
    subtração2 = int(input("Digite o seGundo valor \n"))
    print("O resultado de sua conta é?", subtração1-subtração2)
elif calculadora == 3:
    print("3 = Você escolheu multiplicação")
    multiplicação1 = int(input("Digite o primeiro valor \n"))
    multiplicação2 = int(input("Digite o segundo valor \n"))
    print(multiplicação1*multiplicação2)
    print("O resultado de sua conta é?", multiplicação1*multiplicação2)
elif calculadora == 4:
    print("4 = Você escolheu divisão")
    divisão1 = int(input("Digite o primeiro valor \n"))
    divisão2 = int(input("Digite o segundo valor \n"))
    print(divisão1/divisão2)
    print("O resultado de sua conta é?", divisão1/divisão2)
else:
    print("Você não escolheu nenhuma opção")
    print("Sair do programa")