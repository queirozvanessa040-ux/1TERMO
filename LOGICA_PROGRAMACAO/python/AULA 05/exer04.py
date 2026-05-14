# Exercício 04
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três.
# qualquer opcao diferente sair do menu
opcao = ""

while opcao != "drama" and "suspense" and "romance":
    opcao = input("Digite um gênero para entrar: ").lower()
    if opcao != "drama":
        print(f"Dado '{opcao}' você escolheu o gênero drama!.")
        if opcao != "suspense":
         print(f"Dado '{opcao}' você escolheu o gênero suspense!.")
         if opcao != "romance":
          print(f"Dado '{opcao}' você escolheu o gênero romance!.")
print("Sistema encerrado.")