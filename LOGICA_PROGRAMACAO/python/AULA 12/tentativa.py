# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk 
# 
# # 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha Primeira Janela GUI")
# janela.geometry("800x400") # Tamanho inicial
# 
# # 2. Carregar a imagem original na memória
# caminho_imagem = r"C:\Users\50388990805\Downloads\fundo.png"
# imagem_original = Image.open(caminho_imagem)
# 
# # 3. Criar o Label do fundo (inicialmente vazio)
# lbl_fundo = tk.Label(janela)
# lbl_fundo.place(x=0, y=0, relwidth=1, relheight=1)
# 
# # 🔥 FUNÇÃO NOVA: Redimensiona a imagem dinamicamente
# def redimensionar_fundo(event):
#     # Pega a nova largura e altura da janela atualizada
#     nova_largura = event.width
#     nova_altura = event.height
#     
#     # Redimensiona a imagem original para o novo tamanho da tela
#     imagem_ajustada = imagem_original.resize((nova_largura, nova_altura))
#     
#     # Atualiza a imagem do Label (precisa manter a referência global)
#     global imagem_fundo_tk
#     imagem_fundo_tk = ImageTk.PhotoImage(imagem_ajustada)
#     lbl_fundo.config(image=imagem_fundo_tk)
# 
# # Vincula o evento de redimensionamento da janela à nossa função
# janela.bind('<Configure>', redimensionar_fundo)
# 
# # 4. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão!")
# 
# # 5. Criar os componentes (Texto e Botão)
# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa aula de Tkinter", font=("Arial", 16, "bold"), fg="white", bg="#0a192f")
# 
# btn_clique = tk.Button(
#     janela, 
#     text="Clique Aqui", 
#     font=("Arial", 11, "bold"), 
#     bg="#F02020", 
#     fg="white", 
#     command=mostrar_mensagem,
#     width=20,   
#     height=2    
# )
# 
# # 6. Posicionar os componentes por cima da imagem de fundo
# lbl_titulo.pack(pady=40)
# btn_clique.pack(pady=30)
# 
# janela.mainloop()
