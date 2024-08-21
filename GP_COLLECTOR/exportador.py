import csv
from db.database import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
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

            col_widths = [1.0*inch, 1.0*inch, 1.0*inch, 1.5*inch, 1.5*inch, 1.0*inch]

            y = 710

            c.setFillColor(colors.grey)
            c.rect(50, y, sum(col_widths), 20, fill=True, stroke=False)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 10)
            c.drawString(55, y + 5, "Nome")
            c.drawString(55 + col_widths[0], y + 5, "Fabricante")
            c.drawString(55 + col_widths[0] + col_widths[1], y + 5, "Modelo")
            c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2], y + 5, "Número de Série")
            c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3], y + 5, "Endereço MAC")
            c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3] + col_widths[4], y + 5, "IP")

            y -= 20

            c.setFillColor(colors.black)

            for nome, fabricante, modelo, numero_serie, endereco_mac, ip in printers:
             
            
             font_size = 10  
             max_length = 12  
             col_data = [nome, fabricante, modelo, numero_serie, endereco_mac, ip]
             adjusted_texts = []
            
             # Ajusta tamanho fonte com base no comprimento do texto
             for i, text in enumerate(col_data):
                 if len(text) > max_length:
                    font_size = 8  
                 else:
                    font_size = 10 

                 c.setFont("Helvetica", font_size)
                 adjusted_texts.append(text)

             c.drawString(55, y, nome)
             c.drawString(55 + col_widths[0], y, fabricante)
             c.drawString(55 + col_widths[0] + col_widths[1], y, modelo)
             c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2], y, numero_serie)
             c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3], y, endereco_mac)
             c.drawString(55 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3] + col_widths[4], y, ip)
             y -= 20
            

            c.save()
            messagebox.showinfo("Exportação PDF", "Dados exportados com sucesso para PDF!")  