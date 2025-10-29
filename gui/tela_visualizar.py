import tkinter as tk
from tkinter import ttk

class TelaVisualizar:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizar Vendas")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        frame = ttk.Frame(master, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Vendas Registradas", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("id", "cliente", "produto", "data", "valor")
        self.tree = ttk.Treeview(frame, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(frame, text="Atualizar").pack(side="left", padx=10, pady=10)
        ttk.Button(frame, text="Fechar", command=self.master.destroy).pack(side="right", padx=10, pady=10)
