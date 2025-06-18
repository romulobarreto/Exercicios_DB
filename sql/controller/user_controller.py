from models.user import User
from daos.user_dao import UserDao
from utils.validacao import validar_email, validar_senha

class UserController:

    @staticmethod
    def validar_dados(nome, email, senha):
        # Carrega a lista de 
        pass