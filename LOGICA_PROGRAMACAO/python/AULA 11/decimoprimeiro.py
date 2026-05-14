# Explicação de def: A palavra-chave "def" é usada para definir uma função em Python. Uma função é um bloco de código reutilizável que realiza uma tarefa epecífica.
# return: A palavra-chave "return é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código.

# def nome():
#    nome = input("Digite seu nome:")
#    return nome
# print(f"Olá, {nome()}!")

# def valores():
#    print("Digite três valores: ")
#    a = int(input("Digite o primeiro valor: "))
#    b = int(input("Digite o segundo valor: "))
#    c = int(input("Digite o terceiro valor: "))
#    return a, b, c 
# print(f"Os valores digitados foram: {max(valores())}")

# Reutilizando funções: As funções podem ser reutilizadas em diferentes partes do código, o que torna o código mais organizado e eficiente. No exemplo acima, a função "nome()" é chamada para obter o nome do usuário e a função "valores()" é chamada para obter os três valores digitados pelo usuário.

# nome()
# valores()

## Conceitos Chave
# def: Indica o início da definição da função.
# Nome: Identifica a função para você chamá-la depois.
# Parâmetros: Dados que a função recebe (opcional).
# return: Envia o resultado de volta para quem chamou a função (opcional).
def calcular_dobro(numero):
    return numero * 2
print("O resultado de 5 é: {}".format(calcular_dobro(5)))
# Como usar: resultado = calcular_dobro(5)
print(calcular_dobro(10))