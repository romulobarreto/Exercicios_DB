from controllers.user_controller import *

class UserView:

    @staticmethod
    def login():
        # Carrega lista de usuários
        sucesso, usuarios = UserDao.carregar_usuarios()

        if not usuarios:
            print("\n⚠️ Não há nenhum usuário cadastrado, registre-se!")
            return False, "Sem usuário"

        # Solicita email e senha para login
        print("\n🚻 Faça seu login:")
        email = input("\n👤 Digite seu email: ").strip()
        senha = input("\n🔐 Digite sua senha: ").strip()

        # Chama a verificação de login do controller
        sucesso, mensagem = UserController.login(email, senha)

        if sucesso:
            print(mensagem)
            return True, email
        else:
            print(mensagem)
            return False, mensagem






    @staticmethod
    def cadastrar_usuario():
        # Solicita o input de nome, email e senha
        print("\n🗂️ Informe os seus dados para realizar o cadastro:")
        nome = input("\nDigite o nome do usuário: ").strip().lower()
        email = input("\nDigite o email do usuário: ").strip().lower()
        senha = input("\nDigite a senha do usuário: ").strip()
        confirma_senha = input("\nConfirme a senha escolhida: ").strip()

        # Valida a senha confirmada
        if senha != confirma_senha:
            print("\n⚠️ As senhas estão diferentes.")
            return
        
        # Chama a função de cadastro
        sucesso, mensagem = UserController.cadastrar_usuario(nome, email, senha)

        # Mensagem de retorno
        if sucesso:
            print(mensagem)
            return
        else:
            print(mensagem)
            return
        




    @staticmethod
    def detalhar_usuario(email):
        # Chama a função da controller
        sucesso, lista_formatada = UserController.detalhar_usuario(email)
        # Exibe os dados do usuário
        print(lista_formatada)
        return
    




    @staticmethod
    def editar_usuario(email_mensagem):
        # Carrega os dados do usuário
        sucesso, usuarios = UserDao.carregar_usuarios()

        usuario_cadastrado = next((u for u in usuarios if u.email == email_mensagem), None)

        # Pede input do que alterar
        print("\n🗂️ Escolha a opção que deseja alterar:")
        print("1️⃣ - Nome")
        print("2️⃣ - Email")
        print("3️⃣ - Senha")
        print("4️⃣ - Voltar")

        opcao = input("\nDigite a opção: ").strip()

        if opcao == "1":
            nome = input("\nDigite o novo nome: ").strip().lower()
            email = usuario_cadastrado.email
            senha = usuario_cadastrado.senha

        elif opcao == "2":
            nome = usuario_cadastrado.nome
            email = input("\nDigite o novo email: ").strip().lower()
            senha = usuario_cadastrado.senha

        elif opcao == "3":
            nome = usuario_cadastrado.nome
            email = usuario_cadastrado.email
            senha = input("\nDigite a nova senha: ").strip()
            confirma_senha = input("\nConfirme a senha escolhida: ").strip()

            # Valida a senha confirmada
            if senha != confirma_senha:
                print("\n⚠️ As senhas estão diferentes.")
                return
            

        elif opcao == "4":
            print("✅ Dados mantidos.")
            return
        
        else:
            print("✅ Dados mantidos.")
            return

        # Chama a função do controller
        sucesso, mensagem = UserController.editar_usuario(nome, email, senha, usuario_cadastrado)

        if sucesso:
            if opcao == "1":
                print(mensagem)
                print(f"Nome editado:\nDe: {usuario_cadastrado.nome.title()}\nPara: {nome.title()}")
                return email

            elif opcao == "2":
                print(mensagem)
                print(f"Email editado:\nDe: {usuario_cadastrado.email}\nPara: {email}")
                return email

            elif opcao == "3":
                print(mensagem)
                print(f"Senha editada.")
                return email
        else:
            print(mensagem)
            return
        




    @staticmethod
    def excluir_conta(email_mensagem):
        # Chama a função da controller
        sucesso, mensagem = UserController.excluir_conta(email_mensagem)

        # Retarna a mensagem
        if sucesso:
            print(mensagem)
            return
        else:
            print(mensagem)
            return