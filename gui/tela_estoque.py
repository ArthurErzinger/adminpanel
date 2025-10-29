import tkinter as tk
from tkinter import ttk

class TelaEstoque:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciar Estoque")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        frame = ttk.Frame(master, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Controle de Estoque", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("id", "produto", "quantidade_atual", "quantidade_minima")
        self.tree = ttk.Treeview(frame, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=130)
        self.tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(frame, text="Atualizar Estoque").pack(side="left", padx=10, pady=10)
        ttk.Button(frame, text="Fechar", command=self.master.destroy).pack(side="right", padx=10, pady=10)
