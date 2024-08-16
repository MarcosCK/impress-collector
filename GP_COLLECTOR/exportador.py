import csv
from db.database import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tkinter import filedialog, messagebox

def export_to_csv():    
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            printers = get_printers()
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Impressora", "Fabricante, Modelo, Numero de Serie, Endereco Mac, IP"])
                for nome, fabricante, modelo, numero_serie, endereco_mac, ip in printers:
                    writer.writerow([nome, fabricante, modelo, numero_serie, endereco_mac, ip ])
            messagebox.showinfo("Exportação CSV", "Dados exportados com sucesso para CSV!")

def export_to_pdf():
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            printers = get_printers()
            c = canvas.Canvas(file_path, pagesize=letter)
            c.drawString(100, 750, "Relatório de Impressoras")
            c.drawString(100, 730, "=========================")
            y = 710
            for nome, fabricante, modelo, numero_serie, endereco_mac, ip in printers:
                c.drawString(100, y, f"Nome Impressora: {nome}, Endereco Mac: {endereco_mac}, IP: {ip}")
                y -= 20
            c.save()
            messagebox.showinfo("Exportação PDF", "Dados exportados com sucesso para PDF!")  