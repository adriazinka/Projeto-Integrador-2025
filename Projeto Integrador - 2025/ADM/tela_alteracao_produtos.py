import tkinter as tk
from tkinter import messagebox

# Lista fictícia de produtos (substitua com dados reais de um banco de dados em produção)
produtos = [
    {"id": 1, "nome": "Produto A", "descricao": "Descrição do Produto A", "preco": 25.00},
    {"id": 2, "nome": "Produto B", "descricao": "Descrição do Produto B", "preco": 15.00},
    {"id": 3, "nome": "Produto C", "descricao": "Descrição do Produto C", "preco": 17.00},
    {"id": 4, "nome": "Produto D", "descricao": "Descrição do Produto D", "preco": 30.00},
]

def salvar_alteracoes():
    # Obtém os dados alterados do formulário
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    preco = entry_preco.get()

    # Verifica se os campos estão preenchidos
    if not nome or not descricao or not preco:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Converte preço para float
    try:
        preco = float(preco)
    except ValueError:
        messagebox.showerror("Erro", "Preço deve ser um número válido.")
        return

    # Atualiza os dados do produto
    produto_selecionado = lista_produtos.get(tk.ACTIVE)
    if produto_selecionado:
        produto = next((p for p in produtos if p["nome"] == produto_selecionado), None)
        if produto:
            produto["nome"] = nome
            produto["descricao"] = descricao
            produto["preco"] = preco
            messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
            atualizar_lista_produtos()
        else:
            messagebox.showerror("Erro", "Produto não encontrado.")
    else:
        messagebox.showwarning("Aviso", "Selecione um produto para alterar.")

def preencher_campos():
    # Preenche os campos do formulário com os dados do produto selecionado
    produto_selecionado = lista_produtos.get(tk.ACTIVE)
    if produto_selecionado:
        produto = next((p for p in produtos if p["nome"] == produto_selecionado), None)
        if produto:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, produto["nome"])
            entry_descricao.delete(0, tk.END)
            entry_descricao.insert(0, produto["descricao"])
            entry_preco.delete(0, tk.END)
            entry_preco.insert(0, str(produto["preco"]))
        else:
            messagebox.showerror("Erro", "Produto não encontrado.")
    else:
        messagebox.showwarning("Aviso", "Selecione um produto para alterar.")

def atualizar_lista_produtos():
    # Atualiza a lista de produtos na interface
    lista_produtos.delete(0, tk.END)  # Limpa a lista atual
    for produto in produtos:
        lista_produtos.insert(tk.END, produto["nome"])

def criar_tela_alteracao_produtos():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Alteração de Produtos")
    
    # Rótulo para a lista de produtos
    tk.Label(root, text="Selecione um produto para alterar:").pack(pady=10)
    
    # Lista de produtos
    global lista_produtos
    lista_produtos = tk.Listbox(root, height=10, width=50)
    lista_produtos.pack(pady=10)
    
    # Atualiza a lista de produtos na interface
    atualizar_lista_produtos()
    
    # Botão para preencher os campos com os dados do produto selecionado
    preencher_button = tk.Button(root, text="Preencher Dados", command=preencher_campos)
    preencher_button.pack(pady=5)

    # Rótulos e campos de entrada para editar o produto
    tk.Label(root, text="Nome:").pack(pady=5)
    global entry_nome
    entry_nome = tk.Entry(root, width=50)
    entry_nome.pack(pady=5)
    
    tk.Label(root, text="Descrição:").pack(pady=5)
    global entry_descricao
    entry_descricao = tk.Entry(root, width=50)
    entry_descricao.pack(pady=5)
    
    tk.Label(root, text="Preço:").pack(pady=5)
    global entry_preco
    entry_preco = tk.Entry(root, width=50)
    entry_preco.pack(pady=5)
    
    # Botão para salvar as alterações
    salvar_button = tk.Button(root, text="Salvar Alterações", command=salvar_alteracoes)
    salvar_button.pack(pady=20)
    
    # Inicia o loop da interface gráfica
    root.mainloop()

# Chama a função para criar a tela de alteração
criar_tela_alteracao_produtos()
