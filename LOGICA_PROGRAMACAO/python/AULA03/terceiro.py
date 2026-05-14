#Análises - Função Def (Contraste do print)
# Exemplo01
def saudação(nome):
    return f"Olá, {nome}!"

mensagem = saudação("Vanessa")
print(mensagem)

# Exemplo02
nome = input("Seu nome: ")
idade = int(input("Sua idade: ")) #Converter para texto inteiro
print(f"{nome} tem {idade} anos.")

# Exemplo03
def boas_vindas(nome, cargo):
    print(f'Olá, {nome}! Você é o novo {cargo}.')
boas_vindas("Merlyn", "Desenvolvedora")

# Exemplo 04
def configurar_conexão(servidor, porta=8080):
    print(f"Conectando a {servidor} na porta {porta}...")
    
configurar_conexão("192.168.1.1")                  # Usa a porta 8080
configurar_conexão("10.0.0.1", 3000)               #Usa a porta 3000


# Arredondar casas decimais
# s1 = n1 + n2 + n3 / 3
# round(s1),2