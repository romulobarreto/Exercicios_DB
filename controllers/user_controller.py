from models.user import User
from daos.user_dao import UserDao
from utils.validacao import validar_email, validar_senha
import hashlib

class UserController:

    @staticmethod
    def login(email, senha):
        # Carrega a lista de usuários
        sucesso, usuarios = UserDao.carregar_usuarios()

        #Verifica o email
        usuario_cadastrado = next((u for u in usuarios if u.email == email), None)

        if not usuario_cadastrado:
            return False, f"\n⚠️ O email: {email} não está cadastrado."
        
        
        # Verifica a senha
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        if senha_hash != usuario_cadastrado.senha:
            return False, "\n❌ Senha incorreta."
        
        return True, f"✅ Login realizado com sucesso.\nSeja bem-vindo {usuario_cadastrado.nome.title()}"






    @staticmethod
    def validar_dados(nome, email, senha, email_atual=None):
        # Carrega a lista de 
        sucesso, usuarios = UserDao.carregar_usuarios()

        # Verifica se nome é vazio
        if not nome:
            return False, f"\n⚠️ O nome não pode ser vazio."
        
        # Valida se o email está no padrão
        valida_email = validar_email(email)

        if not valida_email:
            return False, "\n⚠️ Email inválido."
        
        # Verifica se o email é diferente de vazio e se já existe
        if email != email_atual and any(usuario.email == email for usuario in usuarios):
            return False, f"\n🚫 Email já cadastrado."
        
        # Verifica se a senha está dentro do padrão
        valida_senha = validar_senha(senha)

        if not valida_senha:
            return False, "\n🚫 Senha fora dos padrões, requisitos mínimos:\n- 1️⃣ Letra maiúscula\n- 1️⃣ Símbolo\n- 1️⃣ Número"
        
        # Retorna ok
        return True, "✅ Dados validados."
    







    @staticmethod
    def cadastrar_usuario(nome, email, senha):
        # Valida os dados recebidos
        sucesso, mensagem = UserController.validar_dados(nome, email, senha)

        if not sucesso:
            return False, mensagem
        
        # Critografa a senha
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        
        # Cria um usuário
        user = User(None, nome, email, senha_hash)

        # Chama a DAO e salva no banco
        sucesso, mensagem = UserDao.cadastrar_usuario(user)

        if not sucesso:
            return False, mensagem
        else:
            return True, mensagem
        





    @staticmethod
    def detalhar_usuario(email):
        # Carrega a lista de usuarios
        sucesso, usuarios = UserDao.carregar_usuarios()

        usuario_cadastrado = next((u for u in usuarios if u.email == email), None)

        lista_formatada = f"\n🚻 Detalhes do usuário:\nID: {usuario_cadastrado.id}\nNome: {usuario_cadastrado.nome.title()}\nEmail: {usuario_cadastrado.email}"

        return True, lista_formatada
    



    @staticmethod
    def editar_usuario(nome, email, senha, usuario_cadastrado):
        # Verifica se a senha foi alterada
        senha_alterada = senha != usuario_cadastrado.senha

        # Criptografa a senha se necessário
        if senha_alterada:
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        else:
            senha_hash = senha

        # Verifica a senha para passar na validação de dados
        senha_validar = senha if senha_alterada else "SenhaQualquer123@"

        # Valida os dados recebidos
        sucesso, mensagem = UserController.validar_dados(nome, email, senha_validar, usuario_cadastrado.email)

        if not sucesso:
            return False, mensagem
        
        # Cria o usuário
        user = User(usuario_cadastrado.id, nome, email, senha_hash)

        # Chama a DAO
        sucesso, mensagem = UserDao.editar_usuario(user)

        if sucesso:
            return True, mensagem
        else: 
            return False, mensagem
        



    
    @staticmethod
    def excluir_conta(email_mensagem):
        # Chama a DAO
        sucesso, mensagem = UserDao.excluir_usuario(email_mensagem)

        # Exibe retorno
        if sucesso:
            return True, mensagem
        else:
            return False, mensagem