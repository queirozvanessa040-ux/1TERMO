# Exercício 04
# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela.
import os

with open("log.txt", "w") as f:
 f.write("Log de atividades")
with open("log.txt", "r") as f:
 conteudo = f.read()
 print(conteudo)