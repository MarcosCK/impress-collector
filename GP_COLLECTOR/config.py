import tkinter as tk
from tkinter import messagebox

class ConfigDialog(tk.Toplevel):
    def __init__(self, parent, current_interval):
        super().__init__(parent)
        self.title("Configurações")
        self.geometry("300x150")
        self.resizable(False, False)

        self.label_interval = tk.Label(self, text="Intervalo de Atualização (segundos):", font=("Poppins", 10))
        self.label_interval.pack(pady=10)

        self.interval_var = tk.IntVar(value=current_interval // 1000)  # Convertendo para segundos
        self.entry_interval = tk.Entry(self, textvariable=self.interval_var)
        self.entry_interval.pack(pady=5)

        self.button_save = tk.Button(self, text="Salvar", command=self.on_save)
        self.button_save.pack(pady=20)

        self.result = None

    def on_save(self):
        try:
            interval = int(self.interval_var.get()) * 1000  # Convertendo de segundos para milissegundos
            self.result = interval
            self.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")