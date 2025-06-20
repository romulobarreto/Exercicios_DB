from database.database import criar_banco
from views.user_view import *

def menu():
    # Exibe o menu no terminal
    criar_banco()
    while True:
        print("\n🖥️ Sistema de Usuários")
        print("\n📄 Menu:")
        print("1️⃣ - Login")
        print("2️⃣ - Registre-se")
        print("3️⃣ - Sair")

        opcao = input("\nEscolha uma das opções: ").strip()

        if opcao == "1":
            while True:
                sucesso, email_mensagem = UserView.login()
                if sucesso:
                    while True:
                        UserView.detalhar_usuario(email_mensagem)
                        print("\n📑 Opções de cadastro:")
                        print("1️⃣ - Editar Cadastro")
                        print("2️⃣ - Excluir Conta")
                        print("3️⃣ - Logout")

                        opcao_login = input("\nDigite a opção desejada: ").strip()

                        if opcao_login == "1":
                            email_mensagem = UserView.editar_usuario(email_mensagem)
                            continue
                        elif opcao_login == "2":
                            UserView.excluir_conta(email_mensagem)
                            voltar_menu = True
                            break
                        elif opcao_login == "3":
                            voltar_menu = True
                            break
                        else:
                            print("\n⚠️ Opção inválida! Tente novamente.")

                    if voltar_menu:
                        break

                else:
                    while True:
                        print("1️⃣ - Tentar Novamente")
                        print("2️⃣ - Voltar")

                        opcao_login = input("\nDigite a opção desejada: ").strip()

                        if opcao_login == "1":
                            voltar_menu = False
                            break
                        elif opcao_login == "2":
                            voltar_menu = True
                            break
                        else:
                            print("\n⚠️ Opção inválida! Tente novamente.")
                    
                    if voltar_menu:
                        break


        elif opcao == "2":
            UserView.cadastrar_usuario()



        elif opcao == "3":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")

                    




if __name__ == "__main__":
    menu()