import tkinter as tk
from tkinter import ttk

class TelaVenda:
    def __init__(self, master):
        self.master = master
        self.master.title("Registrar Venda")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        frame = ttk.Frame(master, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Registrar Venda", font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(frame, text="Cliente:").pack(anchor="w", pady=5)
        self.cliente_cb = ttk.Combobox(frame, width=30)
        self.cliente_cb.pack(pady=5)

        ttk.Label(frame, text="Produto:").pack(anchor="w", pady=5)
        self.produto_cb = ttk.Combobox(frame, width=30)
        self.produto_cb.pack(pady=5)

        ttk.Label(frame, text="Quantidade:").pack(anchor="w", pady=5)
        self.quantidade_entry = ttk.Entry(frame, width=10)
        self.quantidade_entry.pack(pady=5)

        ttk.Button(frame, text="Registrar Venda", width=20).pack(pady=20)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)
        ttk.Button(frame, text="Fechar", command=self.master.destroy).pack(pady=5)
