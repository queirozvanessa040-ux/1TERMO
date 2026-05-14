# Tratamento de erros com Python
# Erros comuns:
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyWrror: acesso a chave inexistente em dicionário
# except = diz o que deve acontecer caso dê erro no código que você colocou dentro

# Exemplo de tratamento de erros
print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número..."))
    num2 = int(input("Digite o segundo número..."))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")
except ZeroDivisionError:
   print("Erro: Não é possível dividir por zero.")
except ValueError:
   print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except Exception as e:
   print(f"Ocorreu um erro inesperado: {e}")
except NameError:
    print("Erro: Variável não definida.")

# Exemplo

if num1 > 100:
    print("O nímero digitado é maior que 100.")
    for num1 in range(1, 6):
        print(f"{num1} x {num1} = {num1 * num1}")
        if num1 * num1 > 1000:
            print("O resultado da multiplicação é maior que 1000.")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
else:
    print("O número digitado é menor ou igual a 100.")