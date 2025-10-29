import tkinter as tk
from tkinter import ttk
from functions.listar_vendas import list
from datetime import datetime


class TelaVisualizar:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizar Vendas")
        self.master.geometry("700x400")
        self.master.resizable(False, False)

        frame = ttk.Frame(master, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Vendas Registradas", font=("Arial", 14, "bold")).pack(pady=10)

        colunas = ("Codigo_Pedido", "Cliente", "Data_Pedido", "Valor_Fatura", "Status_Fatura")
        self.tree = ttk.Treeview(frame, columns=colunas, show="headings", height=12)

        self.tree.heading("Codigo_Pedido", text="Código")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Data_Pedido", text="Data")
        self.tree.heading("Valor_Fatura", text="Valor (R$)")
        self.tree.heading("Status_Fatura", text="Status")

        for col in colunas:
            self.tree.column(col, width=130, anchor="center")

        self.tree.pack(fill="both", expand=True, pady=10)

        # --- BOTÕES ---
        botoes_frame = ttk.Frame(frame)
        botoes_frame.pack(fill="x", pady=5)

        ttk.Button(botoes_frame, text="Atualizar", command=self.atualizar_tabela).pack(side="left", padx=10)
        ttk.Button(botoes_frame, text="Fechar", command=self.master.destroy).pack(side="right", padx=10)

        # Carrega os dados automaticamente ao abrir
        self.atualizar_tabela()

    def atualizar_tabela(self):
        """Atualiza a Treeview com os dados retornados da função de listagem."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            vendas = list()
        except Exception as e:
            print(f"Erro ao listar vendas: {e}")
            return

        for venda in vendas:
            data_formatada = venda['Data_Pedido'].strftime("%d/%m/%Y %H:%M") if isinstance(venda['Data_Pedido'], datetime) else venda['Data_Pedido']
            self.tree.insert(
                "",
                "end",
                values=(
                    venda.get("Codigo_Pedido", ""),
                    venda.get("Cliente", ""),
                    data_formatada,
                    f"{venda.get('Valor_Fatura', 0):.2f}",
                    venda.get("Status_Fatura", "")
                )
            )