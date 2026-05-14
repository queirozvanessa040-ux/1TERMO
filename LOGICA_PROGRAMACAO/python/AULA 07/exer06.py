# Exercício 06: Criar um arquivo de backup
# Escreva um script que crie um arquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteúdo de "notas.yxy" e escrever no novo arquivo.
import os

with open("notas.txt", "w") as f: # w = write = escrever
  f.write("notas_backup.txt")

with open("notas.txt", "r") as f: # r = read = ler
  conteudo = f.read()
  print(conteudo)

# OU

with open("notas.txt", "r") as notas:
  conteudo = notas.read()
with open("notas_backup.txt", "w") as backup:
  backup.write(conteudo)