from tkinter import Tk, Canvas, Button, simpledialog, messagebox, ttk, Frame, Scrollbar, Frame, Scrollbar, RIGHT, Y, LEFT, BOTH, X, VERTICAL
from db.database import *
from exportador import *
import details

class PrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GP Collect NEXT")
        self.root.geometry("1200x800")
        
        self.create_widgets()
        self.load_printers()
        self.verificacao_att()

    def load_printers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        printers = get_printers()
        for printer in printers:
            self.tree.insert("", "end", values=printer)
            

    def adicionar_impressoras(self):
        dialog = details.CustomDialog(self.root)
        self.root.wait_window(dialog)
        if dialog.result:
            printer_name, printer_ip = dialog.result
            add_printer(printer_name, printer_ip)
            self.load_printers()

    def delete_printer(self):
        selected_item = self.tree.selection()
        if selected_item:
            printer_name = self.tree.item(selected_item[0])["values"][0]
            delete_printer(printer_name)
            self.load_printers()

    def exportar_dados(self):
        file_type = simpledialog.askstring("Exportar Dados", "Escolha o formato de exportação (csv ou pdf):")
        if file_type == "csv":
            export_to_csv()
        elif file_type == "pdf":
            export_to_pdf()
        else:
            messagebox.showwarning("Aviso", "Formato inválido!")    

    def verificacao_att(self):
     printers = get_printers()
     for printer in printers:
        nome, fabricante, modelo, numero_serie, endereco_mac, ip = printer    
        new_data = obter_dados_snmp(ip)
        update_printer_data(nome, new_data['fabricante'], new_data['modelo'], new_data['serial_number'], new_data['endereco_mac'], ip)    
     self.root.after(3000, self.verificacao_att)
       


    def create_widgets(self):
        
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.button_frame = Frame(self.frame)
        self.button_frame.pack(fill=X, padx=30, pady=10)

        self.add_button = Button(self.button_frame,                
                                 text="Adicionar",
                                 compound="top", 
                                 font=("Poppins", 12),
                                 bg="#08B539", 
                                 fg="#FFFFFF",
                                 command=self.adicionar_impressoras)
        self.add_button.grid(row=0, column=0, padx=20)

        self.delete_button = Button(self.button_frame, 
                                    text="Excluir",
                                    compound="top", 
                                    font=("Poppins", 12),
                                    bg="#B50808", 
                                    fg="#FFFFFF",
                                    command=self.delete_printer)
        self.delete_button.grid(row=0, column=1, padx=20)


        self.add_button = Button(self.button_frame, 
                                  text="Exportar Dados",
                                  compound="top", 
                                  font=("Poppins", 12),
                                  bg="#087EB5", 
                                  fg="#FFFFFF",
                                  command=self.exportar_dados)
        self.add_button.grid(row=0, column=2, padx=20) 
        
        self.update_butonn = Button(self.button_frame, 
                                  text="Atualizar",
                                  compound="top", 
                                  font=("Poppins", 12),
                                  bg="#707070", 
                                  fg="#FFFFFF",
                                  command=self.load_printers)
        self.update_butonn.grid(row=0, column=3, padx=20)

        self.config_button = Button(self.button_frame, 
                                  text="Configurações",
                                  compound="top", 
                                  font=("Poppins", 12),
                                  bg="#707070", 
                                  fg="#FFFFFF"
                                  )
        self.config_button.grid(row=0, column=4, padx=20)

         




        self.tree_frame = Frame(self.frame)
        self.tree_frame.pack(fill=BOTH, expand=1)

        style = ttk.Style()
        style.configure("Treeview.Heading", borderwidth=1, relief="solid")

        self.tree = ttk.Treeview(self.tree_frame, columns=("Nome", "Fabricante", "Modelo", "Número de Série", "Endereço MAC", "IP"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Fabricante", text="Fabricante")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Número de Série", text="Número de Série")
        self.tree.heading("Endereço MAC", text="Endereço MAC")
        self.tree.heading("IP", text="IP")
        self.tree.pack(fill=BOTH, expand=1)

        self.tree_scroll = Scrollbar(self.tree_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)


initialize_db()
root = Tk()
app = PrinterApp(root)
root.mainloop()