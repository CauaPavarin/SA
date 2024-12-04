import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

# Base de dados fictícia para armazenamento
usuarios = {"Funcionario": {}, "Cliente": {}}
produtos = []

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Janela Principal
app = ctk.CTk()
app.geometry("1320x780")
app.title("Sistema de Gerenciamento")
app.configure(fg_color="white")

# Habilitar tela cheia
app.state("zoomed")

# Função para exibir a imagem na tela inicial
def exibir_imagem():
    try:
        imagem_original = Image.open("Captura de tela 2024-12-02 231704.png")  # Altere para o caminho correto, se necessário
        imagem_redimensionada = imagem_original.resize((300, 200))  # Ajuste o tamanho conforme necessário
        imagem = ImageTk.PhotoImage(imagem_redimensionada)
        label_imagem = tk.Label(app, image=imagem)
        label_imagem.image = imagem  # Mantém a referência da imagem
        label_imagem.pack(padx=10, pady=20)
    except Exception as e:
        print("Erro ao carregar a imagem:", e)


# Função para estilizar e centralizar botões
def criar_botao(texto, comando):
    return ctk.CTkButton(app, text=texto, command=comando, font=("Arial", 30), height=80, width=350, border_width=1.5, border_color="black", corner_radius=20, text_color="black")
 

# Função para exibir a tela inicial
def tela_inicial():
    for widget in app.winfo_children():
        widget.destroy()


    titulo = ctk.CTkLabel(
        app, 
        text="Bem-vindo a CHAUPI", 
        font=("Helvetica", 52, "bold"),  # Fonte mais estilizada
        text_color="black",  # Cor do texto
        pady=30,
       
        
    )
    titulo.pack(pady=170)

    botao_funcionario = criar_botao("Funcionário", tela_funcionario_opcoes)
    botao_funcionario.pack(pady=20)

    botao_cliente = criar_botao("Cliente", tela_cliente_opcoes)
    botao_cliente.pack(pady=20)

# Tela de opções do Funcionário
def tela_funcionario_opcoes():
    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text="Área do Funcionário", font=("Arial", 50))
    titulo.pack(pady=50)

    botao_login = criar_botao("Login", lambda: tela_login("Funcionario"))
    botao_login.pack(pady=20)

    botao_cadastrar = criar_botao("Cadastrar", lambda: tela_cadastro("Funcionario"))
    botao_cadastrar.pack(pady=20)

    botao_voltar = criar_botao("Voltar", tela_inicial)
    botao_voltar.pack(pady=20)

# Tela de opções do Cliente
def tela_cliente_opcoes():
    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text="Área do Cliente", font=("Arial", 50))
    titulo.pack(pady=50)

    botao_login = criar_botao("Login", lambda: tela_login("Cliente"))
    botao_login.pack(pady=20)

    botao_cadastrar = criar_botao("Cadastrar", lambda: tela_cadastro("Cliente"))
    botao_cadastrar.pack(pady=20)

    botao_voltar = criar_botao("Voltar", tela_inicial)
    botao_voltar.pack(pady=30)

# Tela de cadastro
def tela_cadastro(tipo):
    def cadastrar():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuario and senha:
            if usuario in usuarios[tipo]:
                messagebox.showerror("Erro", "Usuário já cadastrado!")
            else:
                usuarios[tipo][usuario] = senha
                messagebox.showinfo("Sucesso", "Cadastro realizado!")
                tela_inicial()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text=f"Cadastro - {tipo}", font=("Arial", 50))
    titulo.pack(pady=100)

    entrada_usuario = ctk.CTkEntry(app, placeholder_text="Usuário", font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_usuario.pack(pady=20)

    entrada_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*", font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_senha.pack(pady=20)

    botao_cadastrar = criar_botao("Cadastrar", cadastrar)
    botao_cadastrar.pack(pady=20)

    botao_voltar = criar_botao("Voltar", tela_inicial)
    botao_voltar.pack(pady=20)

# Tela de login
def tela_login(tipo):
    def login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuarios[tipo].get(usuario) == senha:
            if tipo == "Funcionario":
                tela_gerenciamento_estoque()
            else:
                tela_catalogo_cliente()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text=f"Login - {tipo}", font=("Arial", 28))
    titulo.pack(pady=50)

    entrada_usuario = ctk.CTkEntry(app, placeholder_text="Usuário", font=("Arial", 16))
    entrada_usuario.pack(pady=10)

    entrada_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*", font=("Arial", 16), width=300)
    entrada_senha.pack(pady=10)

    botao_login = criar_botao("Login", login)
    botao_login.pack(pady=20)

    botao_voltar = criar_botao("Voltar", tela_inicial)
    botao_voltar.pack(pady=20)

# As telas de gerenciamento de estoque e catálogo seguem a mesma lógica, com botões maiores e centralizados.


# Tela de login
def tela_login(tipo):
    def login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuarios[tipo].get(usuario) == senha:
            if tipo == "Funcionario":
                tela_gerenciamento_estoque()
            else:
                tela_catalogo_cliente()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text=f"Login - {tipo}", font=("Arial", 50), width=300)
    titulo.pack(pady=100)

    label_usuario = ctk.CTkLabel(app, text="Usuário:",font=("Arial", 35))
    label_usuario.pack(pady=15)

    entrada_usuario = ctk.CTkEntry(app, placeholder_text="Insira seu usuário",font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_usuario.pack(pady=15,padx=100)

    label_senha = ctk.CTkLabel(app, text="Senha:",font=("Arial", 35))
    label_senha.pack(pady=15)

    entrada_senha = ctk.CTkEntry(app, placeholder_text="Insira sua senha", show="*",font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_senha.pack(pady=15)

    botao_login = ctk.CTkButton(app, text="Login", command=login,font=("Arial", 35),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_login.pack(pady=20)

    botao_voltar = ctk.CTkButton(app, text="Voltar", command=tela_inicial,font=("Arial", 35),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_voltar.pack(pady=20)

    label_ajuda = ctk.CTkLabel(app, text="Insira seu usuário e senha para acessar o sistema.",font=("Arial", 35))
    label_ajuda.pack(pady=20)
    
# Tela de gerenciamento de estoque
def tela_gerenciamento_estoque():
    def adicionar_produto():
        nome = entrada_nome.get()
        preco = entrada_preco.get()
        quantidade = entrada_quantidade.get()

        if nome and preco.isdigit() and quantidade.isdigit():
            produtos.append({"nome": nome, "preco": float(preco), "quantidade": int(quantidade)})
            messagebox.showinfo("Sucesso", "Produto adicionado!")
            atualizar_tabela()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def remover_produto():
        selecionado = tabela.selection()
        if selecionado:
            index = int(selecionado[0])
            produtos.pop(index)
            messagebox.showinfo("Sucesso", "Produto removido!")
            atualizar_tabela()
        else:
            messagebox.showerror("Erro", "Selecione um produto para remover!")

    def atualizar_tabela():
        tabela.delete(*tabela.get_children())
        for i, produto in enumerate(produtos):
            tabela.insert("", "end", iid=i, values=(produto["nome"], produto["preco"], produto["quantidade"]))

    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text="Gerenciamento de Estoque", font=("Arial", 50))
    titulo.pack(pady=30)

    entrada_nome = ctk.CTkEntry(app, placeholder_text="Nome do Produto", font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_nome.pack(pady=15)

    entrada_preco = ctk.CTkEntry(app, placeholder_text="Preço",font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_preco.pack(pady=15)

    entrada_quantidade = ctk.CTkEntry(app, placeholder_text="Quantidade",font=("Arial", 35),width=500,border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    entrada_quantidade.pack(pady=15)

    botao_adicionar = ctk.CTkButton(app, text="Adicionar Produto", command=adicionar_produto,font=("Arial", 25),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_adicionar.pack(pady=15)

    botao_remover = ctk.CTkButton(app, text="Remover Produto", command=remover_produto,font=("Arial", 25),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_remover.pack(pady=15)

    tabela = ttk.Treeview(app, columns=("nome", "preco", "quantidade"), show="headings")
    tabela.heading("nome", text="Nome")
    tabela.heading("preco", text="Preço")
    tabela.heading("quantidade", text="Quantidade")
    tabela.pack(pady=10, fill="x")

    botao_voltar = ctk.CTkButton(app, text="Voltar", command=tela_inicial,font=("Arial", 25),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_voltar.pack(pady=10)

# Tela de catálogo do cliente
# Tela de catálogo do cliente


total_acumulado = 0.0  # Variável global para o total acumulado

def tela_catalogo_cliente():
    global total_acumulado  # Use a variável global para armazenar o total acumulado

    def comprar(produto, quantidade_spinbox):
        nonlocal label_total_acumulado  # Permite modificar o rótulo do total acumulado
        try:
            quantidade = int(quantidade_spinbox.get())
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Insira uma quantidade válida!")
            return

        if quantidade <= produto["quantidade"]:
            produto["quantidade"] -= quantidade
            total = produto["preco"] * quantidade  # Cálculo do preço total
            global total_acumulado
            total_acumulado += total  # Atualiza o total acumulado
            label_total_acumulado.configure(text=f"Total acumulado: R${total_acumulado:.2f}")  # Atualiza o rótulo
            messagebox.showinfo("Sucesso", f"Compra realizada! Preço total: R${total:.2f}")
            tela_catalogo_cliente()  # Atualiza o catálogo
        else:
            messagebox.showerror("Erro", "Quantidade indisponível!")

    for widget in app.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(app, text="Catálogo de Produtos", font=("Arial", 50))
    titulo.pack(pady=20)

    # Rótulo para exibir o total acumulado
    label_total_acumulado = ctk.CTkLabel(app, text=f"Valor total da comprar: R${total_acumulado:.2f}", font=("Arial", 25))
    label_total_acumulado.pack(pady=10)

    frame_catalogo = ctk.CTkFrame(app, fg_color="white")  # Frame para conter o catálogo
    frame_catalogo.pack(pady=10, padx=10, fill="both", expand=True)

    # Configurar a grade
    colunas = 9  # Número de colunas no catálogo
    for i, produto in enumerate(produtos):
        row = i // colunas
        col = i % colunas

        # Frame de cada "card"
        frame_produto = ctk.CTkFrame(frame_catalogo, corner_radius=16, fg_color="#f5f5f5", border_width=1.5, border_color="black")
        frame_produto.grid(row=row, column=col, padx=32, pady=30, sticky="nsew")

        # Nome do produto
        label_nome = ctk.CTkLabel(frame_produto, text=produto["nome"], font=("Arial", 20, "bold"))
        label_nome.pack(pady=5)

        # Preço do produto
        label_preco = ctk.CTkLabel(frame_produto, text=f"Preço: R${produto['preco']:.2f}", font=("Arial", 16))
        label_preco.pack(pady=5)

        # Quantidade disponível
        label_quantidade = ctk.CTkLabel(frame_produto, text=f"Estoque: {produto['quantidade']}", font=("Arial", 16))
        label_quantidade.pack(pady=5)

        # Spinbox para selecionar a quantidade
        quantidade_spinbox = ctk.CTkEntry(frame_produto, placeholder_text="Quantidade", font=("Arial", 16), width=100)
        quantidade_spinbox.pack(pady=1)

        # Botão de compra
        botao_comprar = ctk.CTkButton(
            frame_produto, 
            text="Comprar", 
            command=lambda p=produto, q=quantidade_spinbox: comprar(p, q), 
            font=("Arial", 16)
        )
        botao_comprar.pack(pady=5)

    botao_voltar = ctk.CTkButton(app, text="Voltar", command=tela_inicial, font=("Arial", 25),border_width=1.5,border_color="black", corner_radius=20, text_color="black")
    botao_voltar.pack(pady=20)

    


# Inicia o programa na tela inicial
tela_inicial()

# Loop principal
app.mainloop()