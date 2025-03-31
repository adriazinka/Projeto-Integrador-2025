import tkinter as tk
from tkinter import messagebox
import edit_usuarios
import relatorios_usuarios
import relatorios_produtos
import edit_produtos


def janela_usuarios():
    edit_usuarios.criar_tela()

def janela_relatorio():
     relatorios_usuarios.criar_janela()

def janela_produtos():
     edit_produtos.criar_tela()

def janela_relatorio_prod():
 relatorios_produtos.criar_janela()


def abrir_tela():

    def sair():
            resposta = messagebox.askyesno("Exit", "Are you sure you want to leave??")
            if resposta:
                menu.destroy()

    menu = tk.Tk()
    menu.title("Cores e Sabores")
    menu.config(bg="violet")
    
    frame = tk.Frame(menu)
    frame.pack(expand=True)

 #Criar os Botões 
    botao_usuarios = tk.Button(frame, text="Criação de Usuarios", command=janela_usuarios, width=30,)
    botao_produtos = tk.Button(frame, text="Criação de Produtos", command=janela_produtos, width=30,)
    botao_sair = tk.Button(frame, text="Sair", command=sair, font=("Arial", 12), width=20, height=1, bg="red")
    imagem = tk.PhotoImage(file="ADM/IMGS/projeto.png")
    tk.Label(frame, image=imagem, bg="violet").pack(pady=10)
    frame.config(bg="violet")


    
 
  # Empacotar os botões no frame, um abaixo do outro
    botao_usuarios.pack(pady=10)
    botao_produtos.pack(pady=10)
    botao_sair.pack(pady=10)

 
    # Maximizar a janela
    menu.state('zoomed')

    frame = tk.Frame(menu)
    frame.pack(expand=True)

    menu_bar = tk.Menu(menu)
    menu.config(menu=menu_bar)

    menu_usuarios = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Relatório de Usuarios", menu=menu_usuarios)
    menu_usuarios.add_command(label="Usuarios", command=janela_relatorio)

    menu_produtos = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Relatório de Produtos", menu=menu_produtos)
    menu_produtos.add_command(label="Produtos", command=janela_relatorio_prod)

    menu.mainloop()