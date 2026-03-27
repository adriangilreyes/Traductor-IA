import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "historial_traducciones.db")

# Crear la tabla si no existe
with sqlite3.connect(DB_PATH) as conn: 
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS traducciones( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto_original TEXT, 
            traduccion TEXT,
            src_lang TEXT,
            tgt_lang TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

def guardar_traduccion(texto, traduccion, src, tgt):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO traducciones(texto_original, traduccion, src_lang, tgt_lang) 
            VALUES (?, ?, ?, ?)
        ''', (texto, traduccion, src, tgt))
        conn.commit()

def obtener_historial(limit=10):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT texto_original, traduccion, src_lang, tgt_lang, fecha 
            FROM traducciones
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()  

def mostrar_historial():
    datos = obtener_historial()
    
    if not datos:
        return "No hay traducciones todavía 😅"
    
    # Construimos el texto
    texto = ""
    for t in datos:
        texto += f"{t[0]} → {t[1]} ({t[2]}→{t[3]})\n"
    
    return texto