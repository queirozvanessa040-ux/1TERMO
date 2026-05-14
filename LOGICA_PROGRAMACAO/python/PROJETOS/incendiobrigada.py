print("Bem-Vindo à Brigada de Incêndio!")
print("A partir dos funcionários, será inserido suas informações e de forma controlada verificar equipamentos/ferramentas necessárias da Brigada. \n" + "-"*138)

print("  A seguir, digite quantos funcionários fazem parte do Treinamento da Brigada de Incêndio:")
funcionarios = int(input("Quantidade de funcionários: "))

if funcionarios < 2 or funcionarios > 5:
    print(f"Aviso: O número {funcionarios} está fora do padrão (mínimo 2, máximo 5). Verifique as normas técnicas.")
else:
    print(f"Quantidade de {funcionarios} funcionários registrada com sucesso.")

print("\n Agora insire cadastro de cada funcionário, contendo nome, setor e o status dos treinamentos.")
for i in range(funcionarios):
    print(f"\nCadastro do funcionário {i+1}:")
    nome = input("Nome: ")
    setor = input("Setor: ")
    status_trein = input("Tempo de Treinamento: ")

    print(f"Funcionário {nome} do setor {setor} - Treinamentos: {status_trein}")

print("\nCadastro completo! Desta forma verifique os equipamentos necessários para a Brigada de Incêndio.")
print("")