# Exercício 13

print("Painel de Logio")
senha_correta = "admin123"
tentativas = 3
while tentativas > 0:
    senha = input("Digite a senha do supervisor...")
    if senha == senha_correta:
        print("Acesso Permitido")
        break
    else:
        tentativas -= 1
        print(f"Acesso Negado. Tentativas restantes: {tentativas}")
if tentativas == 0:
    print("Painel Bloqueado")