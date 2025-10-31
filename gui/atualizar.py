import tkinter as tk
from tkinter import ttk, messagebox
from functions.atualizar_quantidade import update

class FrameAtualizar:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback

        frame = tk.LabelFrame(self.master, text="Atualizar Quantidade", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="ID do Produto:").grid(row=0, column=0, sticky="e", pady=2)
        self.id_entry = tk.Entry(frame, width=30)
        self.id_entry.grid(row=0, column=1, pady=2)

        tk.Label(frame, text="Nova Quantidade:").grid(row=1, column=0, sticky="e", pady=2)
        self.quantidade_entry = tk.Entry(frame, width=30)
        self.quantidade_entry.grid(row=1, column=1, pady=2)

        ttk.Button(frame, text="Atualizar Estoque", command=self.atualizar_quantidade).grid(row=2, column=0, columnspan=2, pady=5)

    def atualizar_quantidade(self):
        id_produto = self.id_entry.get().strip()
        nova_quantidade = self.quantidade_entry.get().strip()

        if not id_produto or not nova_quantidade:
            messagebox.showerror("Erro", "Os campos ID do Produto e Nova Quantidade são obrigatórios.")
            return

        try:
            id_produto = int(id_produto)
            nova_quantidade = int(nova_quantidade)
        except ValueError:
            messagebox.showerror("Erro", "ID do Produto e Nova Quantidade devem ser números inteiros.")
            return

        if update(id_produto, nova_quantidade):
            messagebox.showinfo("Sucesso", "Quantidade atualizada com sucesso!")
            self.callback()  # Atualiza a lista de produtos na tela principal
        else:
            messagebox.showerror("Erro", "Não foi possível atualizar a quantidade. Verifique o console para mais detalhes.")
