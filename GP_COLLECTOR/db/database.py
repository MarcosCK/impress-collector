import sqlite3
from easysnmp import Session

DATABASE = 'printers.db'

def initialize_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS printers (
            nome TEXT PRIMARY KEY,           
            fabricante,
            modelo,
            numero_serie,
            endereco_mac,            
            ip TEXT NOT NULL
        )
        ''')
        conn.commit()

def add_printer(printer_name, printer_ip):
   try: 
    data = obter_dados_snmp(printer_ip)
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO printers (nome, fabricante, modelo, numero_serie, endereco_mac, ip) VALUES (?, ?, ?, ?, ?, ?)', 
                       (printer_name, data['fabricante'], data['modelo'], data['serial_number'], data['endereco_mac'], printer_ip))
        conn.commit()
   except Exception as e:
    return ("Erro ao tentar adicionar impressora: {e}")    


def get_printers():
   try:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT nome, fabricante, modelo, numero_serie, endereco_mac, ip FROM printers')
        return cursor.fetchall()
   except Exception as e:
    return ("Erro ao tentar buscar impressoras: {e}")  

def get_printer_counter(printer_name):
     with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT nome, ip FROM printers WHERE nome = ?', (printer_name,))
        return cursor.fetchone()

def delete_printer(printer_name):
   try: 
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM printers WHERE nome = ?', (printer_name,))
        conn.commit()
   except Exception as e:
    return ("Erro ao tentar excluir impressora: {e}")  
   
def update_printer_data(nome, fabricante, modelo, numero_serie, endereco_mac, ip):
   try:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE printers
            SET fabricante = ?, modelo = ?, numero_serie = ?, endereco_mac = ?
            WHERE nome = ? AND ip = ?
        ''', (fabricante, modelo, numero_serie, endereco_mac, nome, ip))
        conn.commit()
   except Exception as e:
     return ("Erro ao tentar atualizar impressora: {e}")    

   
def obter_dados_snmp(ip):
 try:
  session = Session(hostname=ip, community='public', version=2)
  fabricante = '1.3.6.1.2.1.1.5.0'  # Exemplo OID
  modelo = '1.3.6.1.2.1.1.5.0'  # Exemplo OID
  serial_number = '1.3.6.1.2.1.25.1.6.0'  # Exemplo OID
  endereco_mac = '1.3.6.1.2.1.25.1.6.0'  # Exemplo OID
  data = {
        'fabricante': session.get(fabricante).value,
        'modelo': session.get(modelo).value,
        'serial_number': session.get(serial_number).value,
        'endereco_mac': session.get(endereco_mac).value,
    }
  return data
 except Exception as e:
  return ("Erro ao obter dados SNMP: {e}")


 
initialize_db()