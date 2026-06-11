from datetime import date

def verificar_reciclagem(ano_treinamento):
    ano_atual = date.today().year
    # Se o treinamento tiver mais de 2 anos [2]
    if (ano_atual - ano_treinamento) > 2:
        return "Treinamento Vencido! Encaminhar para reciclagem.", False
    else:
        return "Treinamento Válido.", True

print("Bem-Vindo à Brigada de Incêndio!")
print("A partir dos funcionários, será inserido suas informações e de forma controlada verificar equipamentos necessários.\n" + "-"*100)

print("A seguir, digite quantos funcionários fazem parte do Treinamento (mínimo 2, máximo 5):")
funcionarios = int(input("Quantidade de funcionários: "))

# Validação do número de funcionários conforme as normas
if funcionarios < 2 or funcionarios > 5:
    print(f"Aviso: O número {funcionarios} está fora do padrão. Verifique as normas técnicas.")
else:
    print(f"Quantidade de {funcionarios} funcionários registrada com sucesso.")
    
    total_em_dia = 0 # Contador para o relatório final [3]

    for i in range(funcionarios):
        print(f"\n--- Cadastro do funcionário {i+1} ---")
        nome = input("Nome: ")
        
        # Menu de Opções para o Setor conforme solicitado
        print("Escolha o respectivo setor:")
        print("A - Elétrica")
        print("B - Trabalho em Altura")
        print("C - DEV")
        print("D - Logística")
        print("E - Fabricação Mecânica")
        opcao = input("Opção desejada (A-E): ").upper()

        # 2. Verificação de EPI (NR-6) baseada na opção escolhida [1]
        if opcao == "A":
            setor = "Elétrica"
            epis = "- Luvas de alta tensão\n- Botas dielétricas"
        elif opcao == "B":
            setor = "Trabalho em Altura"
            epis = "- Cinturão de segurança\n- Talabarte"
        elif opcao == "C":
            setor = "DEV"
            epis = "- Cadeira ergonômica\n- Apoio para punhos"
        elif opcao == "D":
            setor = "Logística"
            epis = "- Luvas de proteção\n- Botina de segurança"
        elif opcao == "E":
            setor = "Fabricação Mecânica"
            epis = "- Óculos de proteção\n- Protetor auricular"
        else:
            setor = "Não Identificado"
            epis = "Nenhum EPI específico listado."

        # Entrada do ano para verificar reciclagem [1]
        ano_trein = int(input(f"Digite o ano do último treinamento de Brigada do(a) {nome}: "))
        status_msg, em_dia = verificar_reciclagem(ano_trein)
        
        if em_dia:
            total_em_dia += 1

        # Exibição dos dados do funcionário
        print(f"\n>>> Funcionário: {nome} | Setor: {setor}")
        print(f"Status do Treinamento: {status_msg}")
        print(f"EPIs obrigatórios:\n{epis}")

    # 4. Relatório Geral final [2, 3]
    print("\n" + "="*40)
    print("RELATÓRIO GERAL: SESMT")
    print(f"Total de funcionários cadastrados: {funcionarios}")
    print(f"Funcionários com treinamentos em dia: {total_em_dia}")
    print("="*40)