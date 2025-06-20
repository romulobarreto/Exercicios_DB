import sqlite3
from models.user import User

def chamar_banco():
    conexao = sqlite3.connect('database/system.db')
    cursor = conexao.cursor()
    return conexao, cursor
    
class UserDao:

    @staticmethod
    def carregar_usuarios():
        try:
            conexao, cursor = chamar_banco()
            resultado = cursor.execute('SELECT * FROM users')
            dados = resultado.fetchall()
            conexao.close()
            usuarios = [User(*linha) for linha in dados]
            return True, usuarios
        except Exception as e:
            return False, f"\n⚠️ Erro ao buscar usuários: {str(e)}"
    



    @staticmethod
    def cadastrar_usuario(user: User):
        try:
            conexao, cursor = chamar_banco()
            cursor.execute('''
                INSERT INTO users (nome, email, senha) 
                VALUES (?, ?, ?)
            ''', (user.nome, user.email, user.senha,))
            conexao.commit()
            conexao.close()
            return True, "\n✅ Dados cadastrados no banco."
        except Exception as e:
            return False, f"\n⚠️ Erro ao cadastrar usuário: {str(e)}"
        


    @staticmethod
    def editar_usuario(user: User):
        try:
            conexao, cursor = chamar_banco()
            cursor.execute('''
                UPDATE users
                SET nome = ?, email = ?, senha = ?
                WHERE id = ?
            ''', (user.nome, user.email, user.senha, user.id,))
            conexao.commit()
            conexao.close()
            return True, "\n✅ Usuário editado com sucesso."
        except Exception as e:
            return False, f"\n⚠️ Erro ao editar usuário: {str(e)}"
        



    @staticmethod
    def excluir_usuario(email_mensagem):
        try:
            conexao, cursor = chamar_banco()
            cursor.execute('''
                DELETE FROM users
                WHERE email = ?
            ''', (email_mensagem,))
            conexao.commit()
            conexao.close()
            return True, "\n✅ Usuário excluído com sucesso."
        except Exception as e:
            return False, f"\n⚠️ Erro ao excluir usuário: {str(e)}"