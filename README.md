# 🔐 Projeto Sistema de Login - Documentação

## 📌 Visão Geral
Este projeto é um sistema simples de login e gerenciamento de usuários.  
Foi desenvolvido com o objetivo de aplicar conceitos de programação orientada a objetos, padrão arquitetural MVC e integração com banco de dados SQLite.

---

## 📂 Entidades e Estruturas de Dados

### 👤 User
Representa um usuário do sistema.

- **Atributos:**
  - `id`: Identificador único do usuário
  - `nome`: Nome completo
  - `email`: Email do usuário
  - `senha`: Senha criptografada

- **Regras de Negócio:**
  - O email deve ser único.
  - A senha deve ser armazenada de forma segura (criptografada).

---

## 📁 Estrutura do Projeto (Padrão MVC)

### 📂 DataBase
- `database.py`: Função que cria o banco de dados `system.db`.
- `system.db`: Banco de dados do projeto.

### 📂 Models
- `user.py`: Classe que define a entidade `User`.

### 📂 Views
- `user_view.py`: Responsável pela interação com o usuário via terminal.

### 📂 Controllers
- `user_controller.py`: Regras e lógica de manipulação de usuários.

### 📂 DAOs
- `user_dao.py`: Acesso ao banco de dados SQLite.

### 📂 Utils
- `validacao.py`: Funções auxiliares de validação de dados.

### 📂 Main
- `main.py`: Arquivo principal para execução do sistema.

---

## ⚙️ Funcionalidades

- Cadastrar novos usuários
- Editar dados de usuários
- Excluir usuários
- Efetuar login
- Efetuar logout

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem**: Python
- **Banco de Dados**: SQLite
- **Arquitetura**: MVC
- **Interface**: Terminal
- **Bibliotecas**:
  - `sqlite3`: Biblioteca para manipulação do banco de dados SQLite
  - `re`: Validações com expressões regulares
  - `hashlib`: Para criptografia de senhas

---

## 🔄 Fluxo de Uso

1. Usuário abre o sistema via terminal
2. Escolhe entre: login, cadastro ou sair
3. Se logado, pode editar ou excluir seu usuário
4. Todas as ações afetam diretamente o banco de dados SQLite