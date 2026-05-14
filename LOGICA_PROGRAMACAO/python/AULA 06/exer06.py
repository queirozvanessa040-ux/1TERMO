# Exercício 6: Sistema Inteligente de Manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumulados (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo está hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica."
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem "AVISO: Máquina aproximando-se"