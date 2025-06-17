import sqlite3 

def criar_banco():
    with sqlite3.connect('system.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    senha TEXT)
''')