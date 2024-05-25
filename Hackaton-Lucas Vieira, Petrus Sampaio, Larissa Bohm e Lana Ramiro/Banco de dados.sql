
import sqlite3
import os

# Certifique-se de que o diretório do banco de dados existe
os.makedirs('../database', exist_ok=True)

def setup_database():
    conn = sqlite3.connect('../database/database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        tucoins INTEGER DEFAULT 0,
        house_id INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS houses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
    ''')

    # Verifique se as casas já foram inseridas para evitar duplicações
    cursor.execute("SELECT COUNT(*) FROM houses")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO houses (name, price) VALUES ('Casa Simples', 10)")
        cursor.execute("INSERT INTO houses (name, price) VALUES ('Casa de Luxo', 50)")

    conn.commit()
    print("Commit Concluido")
    conn.close()

if _name_ == '_main_':
    setup_database()