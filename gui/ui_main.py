import tkinter as tk
from tkinter import ttk, messagebox
from functions.atualizar_join import read
from gui.adicionar import FrameAdicionar
from gui.atualizar import FrameAtualizar
from gui.deletar import FrameDeletar


class AppEstoque:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque - CRUD Simples")
        self.root.geometry("900x600")
        self.root.configure(bg="#f5f5f5")

        self.criar_tabela()
        self.criar_botoes_principais()
        self.criar_frame_operacoes()
        self.atualizar_lista()

    # ========================
    # TABELA (LISTAGEM)
    # ========================
    def criar_tabela(self):
        frame_tabela = tk.LabelFrame(self.root, text="Produtos em Estoque", padx=10, pady=10, bg="#f5f5f5")
        frame_tabela.pack(fill="x", padx=10, pady=10)

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient="vertical")
        scrollbar_x = ttk.Scrollbar(frame_tabela, orient="horizontal")

        colunas = ("ID", "Nome", "Valor", "Quantidade Atual", "Quantidade Mínima")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=10, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        self.tree.pack(fill="both", expand=True)

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        produtos = read()
        for produto in produtos:
            self.tree.insert("", "end", values=(
                produto['Id_produto'],
                produto['Nome'],
                produto['Valor'],
                produto['quantidade_atual'],
                produto['quantidade_minima']
            ))

    # ========================
    # BOTÕES PRINCIPAIS
    # ========================
    def criar_botoes_principais(self):
        frame_btns = tk.Frame(self.root, bg="#f5f5f5")
        frame_btns.pack(pady=10)

        ttk.Button(frame_btns, text="Atualizar Lista", command=self.atualizar_lista).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btns, text="Adicionar Produto", command=self.abrir_adicionar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_btns, text="Atualizar Quantidade", command=self.abrir_atualizar).grid(row=0, column=2, padx=5)
        ttk.Button(frame_btns, text="Deletar Produto", command=self.abrir_deletar).grid(row=0, column=3, padx=5)

    # ========================
    # ÁREA DE OPERAÇÕES
    # ========================
    def criar_frame_operacoes(self):
        self.frame_operacoes = tk.Frame(self.root, bg="#f5f5f5")
        self.frame_operacoes.pack(pady=10, fill="x")

    def limpar_frame(self):
        for widget in self.frame_operacoes.winfo_children():
            widget.destroy()

    def abrir_adicionar(self):
        self.limpar_frame()
        FrameAdicionar(self.frame_operacoes, self.atualizar_lista)

    def abrir_atualizar(self):
        self.limpar_frame()
        FrameAtualizar(self.frame_operacoes, self.atualizar_lista)

    def abrir_deletar(self):
        self.limpar_frame()
        FrameDeletar(self.frame_operacoes, self.atualizar_lista)
