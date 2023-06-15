while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha != nome_usuario:
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")

print("Usuário e senha registrados com sucesso!")