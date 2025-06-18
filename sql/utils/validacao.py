import re

def validar_email(email):
    # Forma um padrão de email
    padrao_email = r"^[\w]+([\.-]?[\w]+)*@[\w-]+(\.[\w-]+)+$"
    # Retorno do matche entre email e o padrão
    return re.fullmatch(padrao_email, email)



def validar_senha(senha):
    # Forma um padrão de senha
    padrao_senha = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).+$"
    # Retorno do matche entre email e o padrão
    return re.fullmatch(padrao_senha, senha)