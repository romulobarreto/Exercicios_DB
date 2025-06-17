import sqlite3

def chamar_banco():
    conexao = sqlite3.connect('database/system.db')
    cursor = conexao.cursor()
    return conexao, cursor
    
class UserDao:

    @staticmethod
    def detalhar_usuarios():
        # Chama o cursor
        conexao, cursor = chamar_banco()
        # Pesquisa no banco
        resultado = cursor.execute('SELECT * FROM users')
        # Traz o resultado
        dados = resultado.fetchall()
        conexao.close()
        return True, dados
    



    @staticmethod
    def cadastrar_usuario(nome, email, senha):
        # Chama o cursor
        conexao, cursor = chamar_banco()
        # Cadastra a informação no banco
        cursor.execute('''
    INSERT INTO users (nome, email, senha) 
    VALUES (?, ?, ?)''',
    (nome, email, senha,))
        conexao.commit()
        conexao.close()
        return True, "\n✅ Dados cadastrados no banco."