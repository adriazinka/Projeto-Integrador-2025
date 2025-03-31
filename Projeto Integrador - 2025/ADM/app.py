import tkinter as tk
from tkinter import messagebox
import requests
import conf
import menu

root = tk.Tk()
root.title("Área de Login")
root.geometry("500x400")
root.resizable(False, False)
root.config(bg="violet")

def verifica_usuario():
    email = entrada_usuario.get()
    senha = entrada_senha.get()
    
    url_api = f"{conf.url_api}/usuarios/login"
    
    try:
        response = requests.post(url_api, json={"email": email, "senha": senha})
        
        if response.status_code == 200:
            messagebox.showinfo("Good Morning!!", "Welcome the System Mr. ADRIAN!!")
            root.destroy()
            menu.abrir_tela()
        else:
            data = response.json()
            messagebox.showwarning("Login Falhou", data.get("mensagem", "Erro ao autenticar usuário."))
    
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Erro de Rede", "Não foi possível conectar ao servidor.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro de Requisição", f"Erro ao comunicar com o servidor: {e}")

tk.Label(root, text="Área administrativa de estoque", font=("Arial Black", 14, "bold",), bg="violet" ).pack(pady=5)

try:
    imagem = tk.PhotoImage(file="ADM/IMGS/projeto.png")
    tk.Label(root, image=imagem, bg="violet").pack(pady=10)
except Exception as e:
    print(f"Erro ao carregar imagem: {e}")

tk.Label(root, text="E-mail:", font=("Arial", 12), bg="violet"  ).pack(pady=5) 
entrada_usuario = tk.Entry(root, width=40)
entrada_usuario.pack(pady=5)

tk.Label(root, text="Senha:", font=("Arial", 12), bg="violet" ).pack(pady=5)
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", font=("Arial", 12), command=verifica_usuario).pack(pady=15)

root.mainloop()