# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("800x500")
janela.configure(bg="#A285D8")

# Imagem de Fundo
imagem_original = Image.open("C:/Users/50388990805/Downloads/9360941-processo-educacional-on-line-moderno-em-classe-virtual-vetor.jpg")
imagem_redimensionada = imagem_original.resize((800, 600))
imagem_fundo = ImageTk.PhotoImage(imagem_redimensionada)
lbl_background = tk.Label(janela, image=imagem_fundo)
lbl_background.place(relwidth=1, relheight=1)


# 1 - Etapa Componentes
# Labels = Rótulos ou nossos antigos prints
lbL_nome_usuario = tk.Label(janela, text="Digite o seu nome.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_nome_usuario.grid(row=0, column=0, padx=25, pady=25)
lbL_curso = tk.Label(janela, text= "Escolha o seu curso.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_curso.grid(row=1, column=0, padx=25, pady=15)
lbL_escola = tk.Label(janela, text="Escolha a sua escola.:", font=("Arial", 14, "bold"), fg="purple", bg="white")
lbL_escola.grid(row=2, column=0, padx=25, pady=15)

# Entry = Caixa de texto antigos input
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
ent_nome_usuario.grid(row=0, column=0, padx=25, pady=15, sticky="we")

ent_curso = tk.Entry(janela, font=("Arial", 14), width=30)
ent_curso.grid(row=0, column=1, padx=25, pady=15, sticky="we")

ent_escola = tk.Entry(janela, font=("Arial", 14), width=30)
ent_escola.grid(row=2, column=1, padx=25, pady=15, sticky="we")

# combox = curso.
cbx_curso = ttk.Combobox(janela, font=("Arial", 14), width=28, values=["Logística", "EletroEletrônica", "Desenvolvimento de Sistemas", "Fabricação Mecânica"])
cbx_curso.grid(row=1, column=1, padx=25, pady=15)

# combox = escola.
cbx_escola = ttk.Combobox(janela, font=("Arial", 14), width=28, values=["SESI 005", "SESI 408"])
cbx_escola.grid(row=2, column=1, padx=25, pady=15)

# 2 - Cadastro Aluno.
def gerar_cadastro():
    nome = ent_nome_usuario.get()
    curso = cbx_curso.get()
    escola = cbx_escola.get()

    if nome == "" or curso == "" or escola == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos antes de continuar!")
        return
    else:
        messagebox.showinfo("Bem-Vindo", f"Bem-vindo, {nome}! O seu curso é de {curso} e sua escola é {escola}.")

# 3 - Etapa Botão
btn_cadastro = tk.Button(janela, text="Ver Cadastro", font=("Arial", 12, "bold"), command=gerar_cadastro)
btn_cadastro.grid(row=3, column=0, columnspan=2, pady=30)

# 4 - Sair
btn_sair = tk.Button(janela, text="Sair", font=("Arial", 12, "bold"), command=janela.destroy)
btn_sair.grid(row=4, column=0, columnspan=2, pady=10)
def sair():
    resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if resposta:
        janela.destroy()

# 4 - Etapa Loop
janela.mainloop()