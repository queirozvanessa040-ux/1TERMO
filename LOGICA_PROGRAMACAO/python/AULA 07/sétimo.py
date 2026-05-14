# CLEAN CODE
# Para que usar?
# Como usar?

print("Clean Code - AULA 07")
AULA = 7
print(f"Estamos na aula {AULA} de Clean Code")

# Manipulação de arquivos e Texto
texto = " Python é muito legal! "
print(texto.strip().upper()) # PYTHON
print(texto.strip().lower()) # python
print(texto.strip().capitalize()) # Python
print(texto.strip().title()) # Python
print(texto.strip().replace(" ", "_")) # Python
print(texto.strip().split()) # ["python"]

# Escrevendo
with open("notas.txt", "w") as f: # w = write = escrever
  f.write("Estudar Python hoje!")
  f.write("\nLer sobre Clean Code")

# Lendo
with open("notas.txt", "r") as f: # r = read = ler
  conteudo = f.read()
  print(conteudo)

# Execusão de comandos do sistema
import os # importa o módulo os para interagir com o sistema operacional

 # Alt + Shift + setabaixo = colar

# Onde estou?
print(os.getcwd())

# Listar arquivos na pasta
print(os.listdir())
print(os.listdir("..")) # Lista arquivs da pasta Pai
print(os.listdir("..\\..")) # Lista arquivos da pasta Avô
print(os.listdir("C:\\")) # Lista arquivos da raiz do C
print(os.listdir("C:\\Users")) # Lista arquivos da pasta Users
print(os.listdir("C:\\Users\\Public")) # Lista arquivos da pasta Pública

# Outros comandos úteis:
# Criar pasta
os.mkdir("nova_pasta")
# Renomear pasta
os.rename("nova_pasta", "pasta_renomeada")
# Excluir pasta
os.rmdir("pasta_renomeada")

# Exemplo de dicionário
pessoa = {
  "nome": "Alice",
  "idade": "22",
  "cidade": "São paulo"
}
print(pessoa["nome"])

# Exemplo: Desligar o PC (comando para Windows)
with open("desliga.bat", "w") as desligar:
  desligar.write("shutdwon -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")
  # -s = Comando para desligar ou \s
  # -t tempo definido para ser desligado ou \t
  # -a cancelar desligamento \a

with open("desliga.bat", "r") as desligar:
  conteudo = desligar.read()
  print(conteudo)

# Exemplo: Criar um script de limpeza de arquivos
# Escreva um script que liste os arquivos de uma pasta e exclua os arquivos com extensão ".tmp". O script deve exibir uma mensagem para cada arquivo excluído.
pasta = os.listdir()
for arquivo in pasta:
  if arquivo.endswith(".txt"):
    os.remove(arquivo)
    print(f"Arquivo {arquivo} excluído.")
print("Limpeza de arquivos concluída.")

# os.remove = apagar tudo
# os.rmdir = apagar somente a pasta