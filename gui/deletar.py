import tkinter as tk
from tkinter import ttk
from functions.deletar_produto import delete

class FrameDeletar:
    def __init__(self, master, callback):
        self.callback = callback

        self.frame = tk.LabelFrame(master, text="Deletar Produto", padx=10, pady=10)
        self.frame.pack(fill="x", padx=10, pady=5)

        tk.Label(self.frame, text="ID do Produto a Deletar:").grid(row=0, column=0, sticky="e", pady=2)

        self.id_entry = tk.Entry(self.frame, width=30)
        self.id_entry.grid(row=0, column=1, pady=2)

        ttk.Button(
            self.frame,
            text="Excluir Produto",
            command=self.deletar_produto
        ).grid(row=1, column=0, columnspan=2, pady=5)

    def deletar_produto(self):
        id_produto = self.id_entry.get().strip()

        if not id_produto:
            print("ID do produto não pode estar vazio!")
            return

        try:
            delete(id_produto)
            print(f"Produto com ID {id_produto} foi deletado com sucesso!")
            self.callback()  # atualiza a tabela na tela
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
