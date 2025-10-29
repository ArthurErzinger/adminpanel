import tkinter as tk
from tkinter import ttk
from gui.tela_venda import TelaVenda
from gui.tela_visualizar import TelaVisualizar
from gui.tela_estoque import TelaEstoque

class TelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Vendas - Admin")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.frame = ttk.Frame(master, padding=20)
        self.frame.pack(expand=True)

        ttk.Label(self.frame, text="Painel Administrativo", font=("Arial", 16, "bold")).pack(pady=10)

        ttk.Button(self.frame, text="Registrar Venda", width=25, command=self.abrir_venda).pack(pady=5)
        ttk.Button(self.frame, text="Visualizar Vendas", width=25, command=self.abrir_visualizar).pack(pady=5)
        ttk.Button(self.frame, text="Gerenciar Estoque", width=25, command=self.abrir_estoque).pack(pady=5)
        ttk.Button(self.frame, text="Sair", width=25, command=self.master.quit).pack(pady=15)

    def abrir_venda(self):
        TelaVenda(tk.Toplevel(self.master))

    def abrir_visualizar(self):
        TelaVisualizar(tk.Toplevel(self.master))

    def abrir_estoque(self):
        TelaEstoque(tk.Toplevel(self.master))
