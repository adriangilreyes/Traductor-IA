import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BD_PATH = os.path.join(BASE_DIR, "historial_traducciones.db")

print('DB path',BD_PATH)

conn = sqlite3.connect(BD_PATH)
cursor = conn.cursor()

#ver tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tablas:',cursor.fetchall())

#ver datos
cursor.execute("SELECT * FROM traducciones")
print('Datos:',cursor.fetchall())

#contar registros
cursor.execute("SELECT COUNT(*) FROM traducciones")
print('Registros:',cursor.fetchall())

conn.close()