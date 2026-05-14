# Exercício 07

# Coletando os dados do usuário
sensor_porta = input("A porta está aberta ou fechada? ")
botao_emergencia = input("O botão de emergência está ligado ou desligado? ")

# Verificando as condições de segurança
if sensor_porta == "fechada" and botao_emergencia == "desligado":
    print("Segurança confirmada: A máquina pode ser ligada.")
elif sensor_porta != "fechada":
    print("Atenção: A porta precisa estar fechada para operar.")
elif botao_emergencia != "desligado":
    print("Atenção: Desative o botão de emergência primeiro.")
else:
    print("Erro no sistema: Verifique os sensores.")
