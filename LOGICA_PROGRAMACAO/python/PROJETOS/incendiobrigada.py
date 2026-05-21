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
    print("\nCadastro completo! Desta forma verifique qual área cada funcionário pertence para identificar os equipamentos necessários para a Brigada de Incêndio.")if setor == "Elétrica":
    if setor == "Elétrica":
        print("EPIs obrigatórios:")
        print("- Luvas de alta tensão")
        print("- Botas dielétricas")

    elif setor == "DEV":
        print("EPIs obrigatórios:")
        print("- Cadeira ergonômica")
        print("- Apoio para punhos")
        print("- Óculos para proteção visual")

    elif setor == "Logística":
        print("EPIs obrigatórios:")
        print("- Luvas de proteção")
        print("- Botina de segurança")
        print("- Colete refletivo")

    elif setor == "Fabricação Mecânica":
        print("EPIs obrigatórios:")
        print("- Óculos de proteção")
        print("- Protetor auricular")
        print("- Luvas de segurança")
        print("- Botina com biqueira de aço")
    else:
        print("Setor não identificado.")
