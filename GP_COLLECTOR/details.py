import tkinter as tk
from tkinter import messagebox

class CustomDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("GP Collector - Adicionar impressora")
        self.geometry("300x200")
        self.configure(bg="#f0f0f0")

        self.label_title = tk.Label(self, text="Adicionar impressora", font=("Poppins Bold", 14), bg="#f0f0f0")
        self.label_title.pack(pady=10)

        self.frame_form = tk.Frame(self, bg="#f0f0f0")
        self.frame_form.pack(pady=10, padx=20, fill=tk.X)

        self.label_name = tk.Label(self.frame_form, text="Nome intuitivo:", font=("Poppins", 12), bg="#f0f0f0")
        self.label_name.grid(row=0, column=0, pady=5, sticky="w")
        self.entry_name = tk.Entry(self.frame_form, font=("Poppins", 12))
        self.entry_name.grid(row=0, column=1, pady=5)

        self.label_ip = tk.Label(self.frame_form, text="IP Impressora:", font=("Poppins", 12), bg="#f0f0f0")
        self.label_ip.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_ip = tk.Entry(self.frame_form, font=("Poppins", 12))
        self.entry_ip.grid(row=1, column=1, pady=5)

        self.button_frame = tk.Frame(self, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.button_add = tk.Button(self.button_frame, text="Adicionar", command=self.on_add, font=("Poppins", 12), bg="#4caf50", fg="#ffffff")
        self.button_add.pack(pady=10)

        self.result = None

    def on_add(self):
        printer_name = self.entry_name.get() 
        printer_ip = self.entry_ip.get()
        if printer_name and printer_ip:
            self.result = (printer_name, printer_ip)
            self.destroy()
        else:
            messagebox.showwarning("Aviso", "Por favor insira um contador númerico.")