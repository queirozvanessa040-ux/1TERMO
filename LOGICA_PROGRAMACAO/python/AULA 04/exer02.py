# Exercício 02
# Criar um algoritmo para demonstrar a sinalização de um semaforo

print("Bem-Vindo ao trânsito!")
print("Atenção ao semaforo")
print("1 = VERDE")
print("2 = VERMELHO")
print("3 = AMARELO")
semaforo = (input("Digite a opção de cor"))

if semaforo == "1":
    print("VERDE")
elif semaforo == "2":
    print("VERMELHO")
else:
    print("AMARELO")