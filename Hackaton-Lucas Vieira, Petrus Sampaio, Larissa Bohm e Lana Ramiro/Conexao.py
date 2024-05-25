import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('tucoins.db')

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela 'tucoins' se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS tucoins
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogador TEXT NOT NULL,
                tucoins INTEGER NOT NULL)''')


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


cursor.execute("SELECT COUNT(*) FROM tucoins")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO tucoins (id, jogador, tucoins) VALUES (1, 'Fred', 0)")

    conn.commit()
    print("Commit Concluido")
    conn.close()

if __name__ == '_main_':
    setup_database()

print("Banco de dados 'tucoins.db' criado com sucesso!")

