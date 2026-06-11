# Exercício - Crie uma aplicação que faça o cálculo de idade de pessoas.
# Deve perguntar o nome da pessoa e o ano de nascimento

import tkinter as tk
from tkinter import messagebox
from tkinter import font

# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Calculadora de Idade")
janela.geometry("750x500")  # Aumentei a altura para 500 para caber tudo empilhado
janela.configure(bg="#A285D8")

# 1 - Etapa Componentes (Alterado o row e column para empilhar)
lbL_nome_usuario = tk.Label(janela, text="Digite o seu nome.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_nome_usuario.grid(row=0, column=0, padx=25, pady=15, sticky="w")

ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=1, padx=25, pady=15, sticky="we")

lbL_nascimento = tk.Label(janela, text="Digite o seu ano de nascimento.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_nascimento.grid(row=1, column=0, padx=25, pady=15, sticky="w")

ent_nascimento = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nascimento.grid(row=1, column=1, padx=25, pady=15, sticky="we")

lbL_ano_atual = tk.Label(janela, text="Digite o ano atual.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_ano_atual.grid(row=2, column=0, padx=25, pady=15, sticky="w")

ent_ano_atual = tk.Entry(janela, font=("Arial", 14), width=30)
ent_ano_atual.grid(row=2, column=1, padx=25, pady=15, sticky="we")


# 2 - Cálculo de Idade
def calcular_idade():
    nome = ent_nome_usuario.get()
    nascimento = ent_nascimento.get()
    ano_atual = ent_ano_atual.get()

    # Ajustado para travar caso o ano atual também falte
    if nascimento == "" or ano_atual == "":
        messagebox.showwarning("Aviso", "Por favor, preencha o ano de nascimento e o ano atual.")
    else:
        resultado = int(ano_atual) - int(nascimento)
        messagebox.showinfo("Resultado", f"{nome}, a sua idade é de {resultado} anos.")

# Botão Idade (Atualizado columnspan para 2, já que agora temos 2 colunas)
btn_calcular = tk.Button(janela, text="Calcular Idade", font=("Arial", 14, "bold"), fg="white", bg="purple", command=calcular_idade)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=20)

# Botão Sair
def sair():
    janela.destroy()
btn_sair = tk.Button(janela, text="Sair", font=("Arial", 14, "bold"), fg="white", bg="red", command=sair)
btn_sair.grid(row=4, column=0, columnspan=2, pady=10)

# 3 - Etapa Loop/Final
janela.mainloop()
