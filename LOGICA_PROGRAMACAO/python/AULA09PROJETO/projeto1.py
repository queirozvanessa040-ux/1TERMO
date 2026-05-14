# Projeto Cancela Automática
# Criar um algoritmo que consiga gerenciar entrada e saída de veículos, inserindo valores por hora permanecida.
# A forma de entrada e saída deve ser especifica e permitir o usuário inserir os dados necessários para registro do veículo.
# Passos
# 1 - Pressionar botão, imprimir um ticket
# Calcular tempo de permanência
# Pagar o ticket
# Devolver ticket na saída
# Liberar e fechar cancelas

# 2 - Acesso por TAGs (Sem parar, Connect Car..)
# Calcular tempo de permanência
# Gerar pagamento em fatura
# Liberar e fechar cancelas

# 3 - Problematização
# Verificar sinal de transmissão da TAG
# Verificar acesson por ticket ou tag ao mesmo tempo
# Perdeu ticket (levantar informações)
# Problemas com cancelas

print("---Bem-vindo ao Shopping SENAI---")
print("---Ao adentrar no estacionamento, escolha sua forma de entrada---")
entrada = int(input("---Digite a sua forma de escolha 1 = Ticket 2 = TAG ou 3 = problema---"))

if entrada == 1:
    tperm = int(input("Digite o seu tempo de permanência: \n"))
    vhora = 3
    total = (tperm * vhora) / 2
    print(f"O valor total de sua permanência foi: {total:.2f}")
    print(f"Agradecemos pela sua vinda! Volte sempre!")
elif entrada == 2:
    vtemp = int(input("O seu tempo de permanência foi: \n"))
    vhora = 3
    vtotal = (vtemp * vhora) / 2
    print("Agradecemos pela sua vinda! Volte sempre!")
    print(f"O valor de sua fatura foi: {vtotal:.2f}")
else:
    print("---CENTRAL DE AJUDA E SUPORTE---")
    print("1 - Falha no sinal da TAG")
    print("2 - Conflito: Tentou usar TAG e Ticket juntos")
    print("3 - Perdi meu ticket")
    print("4 - Cancela travada ou sem energia")
    print("5 - Outros...")
    problema = int(input("Selecione o problema ocorrido: "))

    if problema == 1:
        print("Sensor de metal detectou o carro, mas a TAG não respondeu.")
        print("Por favor, aperte o botão e retire o Ticket físico.")

    elif problema == 2:
        print("Detectamos leitura de TAG e emissão de Ticket em conjunto.")
        print("Prioridade para TAG! O ticket físico foi cancelado no sistema.")

    elif problema == 3:
        print("Perda de Ticket informada.")
        placa = input("Digite a placa do seu veículo para busca no sistema: ")
        print(f"Placa {placa} localizada! Gerando segunda via com base na câmera.")

    elif problema == 4:
        print("Falha mecânica ou elétrica na cancela.")
        print("Sensor de segurança ativo. Liberação manual pelo operador autorizada.")
    elif problema == 5:
        prob = input("Use o audío para dizer o problema e entrar em contato com a(o) atendente")
    else:
        print("Opção de problema inválida!")