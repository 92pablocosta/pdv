
def register_user(username, password):
    """Registra um novo usuário se o nome de usuário ainda não estiver em uso."""
    users = load_users()
    
    if username in users:
        print("Usuário já existe!")
        return False
    
    with open('cliente.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    
    print("Usuário registrado com sucesso!")
    return True

def login_user(username, password):
    """Verifica se o nome de usuário e a senha estão corretos."""
    users = load_users()
    
    if username not in users:
        print("Usuário não encontrado!")
        return False
    
    if users[username] == password:
        print(f"Login bem-sucedido. Bem vindo {username}!")
        return True
    else:
        print("Senha incorreta!")
        return False

def load_users():
    """Carrega os usuários do arquivo de texto e retorna um dicionário."""
    users = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    except FileNotFoundError:
        # O arquivo não existe ainda, retornamos um dicionário vazio
        pass
    
    return users

def main():
    while True:
               
        print("\n1. Registrar")
        print("2. Login")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            login_user(username, password)
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
