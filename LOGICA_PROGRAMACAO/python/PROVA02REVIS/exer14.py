# Exercício 14

print("Simulador de Estoque")
estoque = 100
while True:
    print("\nMenu:")
    print("1. Adicionar itens")
    print("2. Adicionar itens")
    print("3. Sair")
    escolha = input("Escolha uma opção (1, 2 ou 3)...")


    if escolha == 1:
        quantidade = int(input("Digite a quantidade itens a adiconar..."))
        estoque += quantidade
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == 2:
        quantidade = int(input("Digite a quantidade itens a adiconar..."))
        estoque -= quantidade
        print(f"Estoque atualizado: {estoque} itens")
        if estoque < 10:
            print("Estoque Crítico!")
    elif escolha == 3:
        print("Saindo do simulado de estoque.")
        break
    else:
        print("Opção inválida. Tente novamente.")