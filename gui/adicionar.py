import tkinter as tk
from tkinter import ttk, messagebox
from functions.adicionar_produto import add

class FrameAdicionar:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback

        frame = tk.LabelFrame(master, text="Adicionar Produto", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="e", pady=2)
        self.nome_entry = tk.Entry(frame, width=30)
        self.nome_entry.grid(row=0, column=1, pady=2)

        tk.Label(frame, text="Valor (R$):").grid(row=1, column=0, sticky="e", pady=2)
        self.valor_entry = tk.Entry(frame, width=30)
        self.valor_entry.grid(row=1, column=1, pady=2)

        tk.Label(frame, text="Quantidade Atual:").grid(row=2, column=0, sticky="e", pady=2)
        self.qnt_atual_entry = tk.Entry(frame, width=30)
        self.qnt_atual_entry.grid(row=2, column=1, pady=2)

        tk.Label(frame, text="Quantidade Mínima:").grid(row=3, column=0, sticky="e", pady=2)
        self.qnt_minima_entry = tk.Entry(frame, width=30)
        self.qnt_minima_entry.grid(row=3, column=1, pady=2)

        ttk.Button(frame, text="Salvar Produto", command=self.adicionar_produto).grid(row=4, column=0, columnspan=2, pady=5)

    def adicionar_produto(self):
        nome = self.nome_entry.get().strip()
        valor_str = self.valor_entry.get().strip()
        qnt_atual_str = self.qnt_atual_entry.get().strip()
        qnt_minima_str = self.qnt_minima_entry.get().strip()

        if not all([nome, valor_str, qnt_atual_str, qnt_minima_str]):
            messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios.")
            return

        try:
            valor = float(valor_str.replace(',', '.'))
            qnt_atual = int(qnt_atual_str)
            qnt_minima = int(qnt_minima_str)
        except ValueError:
            messagebox.showerror("Erro de Formato", "Verifique se os valores numéricos estão corretos.")
            return

        if add(nome, valor, qnt_atual, qnt_minima):
            messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")
            self.callback()  # Atualiza a lista de produtos
        else:
            messagebox.showerror("Erro de Banco de Dados", "Não foi possível adicionar o produto. Verifique o console.")
