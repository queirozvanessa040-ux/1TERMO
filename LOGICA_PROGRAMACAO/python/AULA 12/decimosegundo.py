# TKINTER
# CONCEITO TKINTER: O Tkinter é uma biblioteca padrão do Python projetada para criar interfaces gráficas de usuário (GUIs) em aplicações desktop, permitindo o desenvolvimento de programas interativos com elementos como janelas, botões, menus, formulários e widgets personalizados de forma simples e eficiente; ele é especialmente útil para protótipos rápidos, ferramentas educativas ou aplicativos básicos que necessitam de uma interface visual sem depender de dependências externas complexas, facilitando a criação de itens como calculadoras gráficas ou editores de texto, e opera de maneira multiplataforma em sistemas como Windows, macOS e Linux.

# WIDGET: É um elemento gráfico que compõe a interface do usuário, como botões, rótulos, caixas de texto, etc., permitindo a interação do usuário com a aplicação.

# Componentes Widgets
# tk: Tk() # Janela
# Ib: Label() # Rótulo
# bt: Button() # Botão
# et: Entry() # Caixa de texto

# import tkinter as tk
# from tkinter import messagebox
# 
# # 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha Primeira Janela GUI")
# janela.geometry("800x400") # Largura x Altura
# 
# # 2. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão!")
# 
# # 3. Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa aula de Tkinter", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text="Clique Aqui", font=("Arial", 11), 
# bg="#A020F0", fg="white", command=mostrar_mensagem)
# 
# # 4. Posicionar os componentes
# lbl_titulo.pack(pady=50)
# btn_clique.pack(pady=40, ipadx=50, ipady=20)
# 
# # 5. Iniciar o loop da janela
# janela.mainloop()



#import tkinter as tk
#from tkinter import messagebox
#def saudar_usuario():
#    # .get() = serve para buscar o texto que vamos digitar
#    
#    nome = campo_nome.get()
#
#    if nome == "":
#        messagebox.showwarning("Aviso", "Por favor, digite seu nome!")

#    else:
#        messagebox.showinfo("Saudações Alunos", f"Olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas")

# Configurações da janela
#app = tk.Tk()
#app.title("Exemplo 1")
#app.geometry("350x200")

# Componentes
#ibl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
#ibl_instrucao.pack(pady=10)

#campo_nome = tk.Entry(app, font=("Arial", 12))
#campo_nome.pack()

#btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
#btn_enviar.pack(pady=15)

#app.mainloop()

# Exercício: Crie uma interface gráfica que calcule a média de três notas digitais pelo usuário. A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média. Ao clicar no botão, a média deve ser exibida em uma mensagem.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calcular_notas():
    nota1 = campo_nota1.get()
    nota2 = campo_nota2.get()
    nota3 = campo_nota3.get()

    if nota1 == "" or nota2 == "" or nota3 == "":
        messagebox.showwarning("Aviso", "Por favor, digite todas as notas!")
    else:
        media = (float(nota1) + float(nota2) + float(nota3)) / 3
        messagebox.showinfo("Média", f"A média das notas é: {media:.2f}")
    if media >= 50:
        messagebox.showinfo("Resultado", "Parabéns! Você foi aprovado!")
    if media < 50:
        messagebox.showinfo("Resultado", "Infelizmente, você foi reprovado!")

# Configurações da janela
app = tk.Tk()
app.title("Calculadora de Média")
app.geometry("1500x700")

# Configura as colunas elásticas para manter tudo no centro
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# 3. Criar o Label do fundo
lbl_fundo = tk.Label(app)
lbl_fundo.place(x=0, y=0, relwidth=1, relheight=1)

caminho_imagem = r"C:\Users\50388990805\Downloads\fundo.jpeg"
imagem_original = Image.open(caminho_imagem)

def redimensionar_fundo(event):
    nova_largura = event.width
    nova_altura = event.height
    imagem_ajustada = imagem_original.resize((nova_largura, nova_altura))
    global imagem_fundo_tk
    imagem_fundo_tk = ImageTk.PhotoImage(imagem_ajustada)
    lbl_fundo.config(image=imagem_fundo_tk)

app.bind('<Configure>', redimensionar_fundo)

lbl_instrucao = tk.Label(app, text="Digite as três notas abaixo:", font=("Arial", 16, "bold"), fg="white", bg="#ec1a1a")
lbl_instrucao.grid(row=0, column=0, columnspan=2, pady=30, ipady=15, sticky="ew")

lbl_nota1 = tk.Label(app, text="Digite a primeira nota:", font=("Arial", 14), fg="white", bg="#0a192f")
lbl_nota1.grid(row=1, column=0, padx=20, pady=25, sticky="e")
campo_nota1 = tk.Entry(app, font=("Arial", 35), width=10)
campo_nota1.grid(row=1, column=1, padx=20, pady=25, sticky="w")

lbl_nota2 = tk.Label(app, text="Digite a segunda nota:", font=("Arial", 14), fg="white", bg="#0a192f")
lbl_nota2.grid(row=2, column=0, padx=20, pady=25, sticky="e")
campo_nota2 = tk.Entry(app, font=("Arial", 35), width=10)
campo_nota2.grid(row=2, column=1, padx=20, pady=25, sticky="w")

lbl_nota3 = tk.Label(app, text="Digite a terceira nota:", font=("Arial", 14), fg="white", bg="#0a192f")
lbl_nota3.grid(row=3, column=0, padx=20, pady=25, sticky="e")
campo_nota3 = tk.Entry(app, font=("Arial", 35), width=10)
campo_nota3.grid(row=3, column=1, padx=20, pady=25, sticky="w")

btn_calcular = tk.Button(app, text="Calcular Média", font=("Arial", 12, "bold"), bg="#F02020", fg="white", command=calcular_notas)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=30, ipadx=40, ipady=10)

btn_close = tk.Label(app, text="Fechar", font=("Arial", 10), bg="#0a192f", fg="white", cursor="hand2")
btn_close.grid(row=7, column=0, columnspan=3, pady=30, ipadx=20, ipady=5)
btn_close.bind("<Button-1>", lambda e: app.destroy())

app.mainloop()
