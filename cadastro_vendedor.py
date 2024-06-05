def registro_vendedor(username, password):
    """Registra um novo usuário se o nome de usuário ainda não estiver em uso."""
    vendedor = load_users()
    
    if username in vendedor:
        print("Usuário já existe!")
        return False
    
    with open('vendedor.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    
    print("Usuário registrado com sucesso!")
    return True

def login_vendedor(username, password):
    """Verifica se o nome de usuário e a senha estão corretos."""
    vendedor = load_users()
    
    if username not in vendedor:
        print("ERRO: Usuário não encontrado, tente novamente")
        return False
    
    if vendedor[username] == password:
        print(f"Login bem-sucedido. Bem vindo {username}!")
        return True
    else:
        print("Senha incorreta!")
        return False
    

def load_users():
    """Carrega os usuários do arquivo de texto e retorna um dicionário."""
    vendedor = {}
    try:
        with open('vendedor.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                vendedor[username] = password
    except FileNotFoundError:
        # O arquivo não existe ainda, retornamos um dicionário vazio
        pass
    
    return vendedor

def main():
    while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            registro_vendedor(username, password)
        elif choice == '2':
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            login_vendedor(username, password)
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
