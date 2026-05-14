# Exercício 05
# Crie um dicionário com informações sobre uma pessoa e acesse um valor usando uma chave.

pessoa = {
  "nome": "Vanessa",
  "idade": "16",
  "nascimento": "2009",
  "profissão": "Estudante",
  "cidade": "Limeira"
}
print(pessoa["nome"], pessoa["idade"], pessoa["nascimento"], pessoa["profissão"], pessoa["cidade"])



with open("notas.txt", "w") as f: # w = write = escrever
  f.write("notas_backup.txt")

with open("notas.txt", "r") as f: # r = read = ler
  conteudo = f.read()
  print(conteudo)